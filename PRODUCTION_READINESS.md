# El Corderito — preparación para operación comercial
Actualizado: 2026-10-25

**Estado: beta funcional / piloto supervisado. No se considera aún producción.**

## Verificado en las pruebas iniciales
- [x] Administrador y empleado con cuentas separadas y permisos diferenciados.
- [x] Alta de inventario y descuento automático de ingredientes al registrar ventas.
- [x] Turnos, cortes de caja y comprobantes históricos.
- [x] Promociones 2× y 3× con descuentos calculados por el servidor.
- [x] Historial de ventas, calendario y reportes por empleado/periodo.
- [x] Inicio de sesión persistente y navegación Atrás dentro de Android.
- [x] La APK compila y su firma debug puede verificarse técnicamente.

## Necesario antes de usar con ventas reales
- [ ] **Respaldo y restauración verificados**: conservar copias automáticas externas de la base de datos y probar la recuperación completa con inventario, cuentas, ventas y turnos.
- [ ] **Firma estable de la APK**: configurar en GitHub Actions los secretos de firma privada; conservar el respaldo privado. Sustituir la APK debug por release estable antes de distribuirla.
- [ ] **Seguridad de cuentas**: activar protección contra contraseñas filtradas en Supabase Authentication; revisar expiración/revocación de sesiones, acceso del personal y controles de XSS.
- [ ] **Pruebas de resistencia**: interrupción de internet durante cobro, reintentos, ventas repetidas, falta de inventario, sincronización de dos dispositivos, cierre de turno con diferencias y pérdida de señal al registrar movimientos.
- [ ] **Flujo de recuperación**: documentar cómo continuar ventas manuales ante caída del servicio y reconciliar los movimientos al reconectar.
- [ ] **Ensayo de operación real**: jornadas completas con cierre y revisión de caja; conciliación de efectivo, transferencias, productos y mermas.
- [ ] **Precios y recetas definitivas**: porciones exactas, costos actualizados, inventario físico inicial y márgenes.
- [ ] **Acceso por trabajador**: cuentas y contraseñas independientes, alta/baja de empleados, rotación de claves y registro de incidencias.
- [ ] **Criterios comerciales/fiscales**: definir emisión de comprobantes al cliente, CFDI cuando proceda, política de privacidad y manejo de datos conforme a la operación local.
- [ ] **Android UX**: confirmar nitidez de icono y pantalla de arranque v0.14.1 en el dispositivo objetivo.

## Objetivo de salida de beta
Pasar a producción solo después de completar los requisitos críticos, resolver defectos encontrados y verificar copia y recuperación de datos. Las pruebas previas prueban funcionalidad básica, no disponibilidad ni recuperación ante pérdida de información.

Esta lista contiene exclusivamente criterios técnicos y operativos. No guarda credenciales, contraseñas ni datos personales.
