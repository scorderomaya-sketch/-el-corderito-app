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
- [ ] C3 conectar editor exclusivo del administrador, catálogo del empleado y resumen de cobro.
- [ ] C4 ejecutar tests de interfaz, comprobar despliegue de GitHub Pages.
- [ ] C5 validar con teléfono: 1 combo ficticio sin activar de forma comercial.

## Incidencias
- 2026-10-26: Error de transmisión al recuperar respuesta larga de Supabase. Mitigación aplicada: cuatro fragmentos SQL de 1600 caracteres cada uno.
- 2026-10-26: Error del lector de respuestas SQL: coincidía con la primera etiqueta `<untrusted-data>` explicativa, no con el bloque real. Corregido recuperando la segunda etiqueta tras `\n\n`. Solo afectó lectura, no BD.
- 2026-10-26: C1 y C2 completados; no se generaron combos permanentes ni se modificaron ventas en las pruebas.
