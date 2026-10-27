# El Corderito — checkpoint de implementación de combos

Fecha: 2026-10-26. Rama: main. OBJETIVO: combos configurables por administrador, venta atómica e inventario por componentes.

## Regla de recuperación
1. Leer ESTE archivo antes de efectuar cualquier cambio.
2. Consultar Supabase para verificar el estado real. No suponer que una llamada previa se aplicó.
3. No activar combos reales, no borrar ventas ni modificar inventario real durante pruebas.
4. Ejecutar pruebas de escritura con transacción revertida (rollback deliberado).
5. Actualizar este documento después de cada etapa verificable; registrar errores y rollback.
6. Mantener funcionando las ventas de productos existentes, ofertas 2×/3×, sesiones y reportes.

## C0: auditoría inicial — CONFIRMADA
- BD conectada. Tablas existentes: `public.combos`, `public.combo_components`, `public.combo_change_history`.
- Columna `public.sale_items.combo_snapshot` existente; función `private.admin_save_combo` creada en el intento anterior (verificar permisos y funcionamiento).
- `public.sales`: 2 registros antes de retomar. `public.combos`: 0 registros. No hay combos creados/activos.
- Web `index.html` branch main: SHA blob `00e0a1c565b7781d3857e5db80e21c8060c58c9b`; aún no tiene editor visual ni cobro de combos.
- Error anterior: la solicitud que quería devolver la definición entera de `private.pos_checkout` falló/interrumpió transmisión, no se aplicó integración de cobro.
- Solución: recuperar definición en fragmentos cortos o adaptar función mediante migraciones verificadas. Evitar respuestas SQL largas.

## Etapas
- [x] C0 auditar BD y web sin modificar datos reales.
- [x] C1 función de cobro actualizada (migración `corderito_c1_checkout_nested_combo_components_and_snapshot`): precio independiente, ingredientes expandidos, snapshot y validación de recetas; conserva POS anterior.
- [x] C2 prueba SQL transaccional revertida: 2 combos (2×$120) + producto normal ($99) = $339; ingredientes A 20→15, B 20→18; snapshot de dos componentes; reintento idempotente sin doble consumo; edición denegada a empleado.
- [x] C3 editor de combos en `index.html`, guardado RPC solo admin, selección de componentes, precio libre, activación opcional, catálogo POS; no se activó ningún combo real. Se corrigió conservación de formularios y se impidió editar combos desde el módulo normal de precios.
- [x] C4 pruebas de interfaz simulada (8 comprobaciones), venta desde empleado de 3 combos por $375, decremento A 20→17 y B 20→14, snapshot, bloqueo de combos anidados y promociones 2×/3× sobre combos, denegación de cambios desde empleado. Todas las ventas y productos de prueba fueron revertidos. Despliegue GitHub Pages `40436221575`: **success**.
- [ ] C5 verificación manual en Android: abrir `Más → Creador de combos`, crear un combo **inactivo** y comprobar componentes; si se activa para prueba, comprobar cobro con ambos roles y contrastar inventario. Requiere acción del propietario.

## Incidencias
- 2026-10-26: Error de transmisión al recuperar respuesta larga de Supabase. Mitigación aplicada: cuatro fragmentos SQL de 1600 caracteres cada uno.
- 2026-10-26: Error del lector de respuestas SQL: coincidía con la primera etiqueta `<untrusted-data>` explicativa, no con el bloque real. Corregido recuperando la segunda etiqueta tras `\n\n`. Solo afectó lectura, no BD.
- 2026-10-26: C1 y C2 completados; no se generaron combos permanentes ni se modificaron ventas en las pruebas.

## Estado confirmado tras C4
- Ventas almacenadas: 2 (sin modificación).
- Combos creados: 0; combo_components: 0; productos temporales: 0.
- Cobro normal y promoción 2×/3× de productos individuales conservados.
- La nueva interfaz web quedó publicada en GitHub Pages. No requiere reinstalar APK WebView.
- Cualquier fallo nuevo debe registrarse aquí con etapa, descripción, resultado esperado/actual, verificación y solución. Estado de C5 pendiente de prueba manual.
