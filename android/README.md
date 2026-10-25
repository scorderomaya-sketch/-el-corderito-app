# El Corderito v0.14 — APK Android (beta)

Aplicación Android de prueba. El panel web se actualiza desde GitHub Pages y los datos de ventas e inventario siguen en Supabase.

## Cambios de v0.14
- Icono oficial: cabeza del corderito sobre fondo crema, generado desde la mascota ya utilizada en `index.html` mediante `tools/generate_android_icons.py`.
- Pantalla sin conexión con la mascota oficial y botón para reintentar.
- Atrás navega por el historial de pestañas y, si ya no hay historial, deja la tarea en segundo plano para conservar la sesión.
- Mismo `applicationId`: `mx.elcorderito.mobile`; `versionCode=14`.
- Configuración preparada para firmar las próximas versiones con una **clave de firma Android estable**, fuera del repositorio.

## Construcción por GitHub Actions

La automatización `.github/workflows/build-android-apk.yml` puede ejecutarse en **GitHub → Actions → Build El Corderito APK → Run workflow**. También corre cuando cambian archivos Android o de compilación.

Si todavía no hay secretos de firma, crea una APK **debug temporal** (`El_Corderito_v0.14-debug.apk`). Sirve para pruebas, pero no garantiza actualizaciones instalables encima entre distintas ejecuciones.

## Activar la firma estable (recomendado antes de distribuir)

El administrador debe guardar la clave `.jks` privada y configurarla como secreto de GitHub. **Nunca publiques esta clave ni las contraseñas en el repositorio.**

1. En GitHub entra a este repositorio.
2. Abre **Settings → Secrets and variables → Actions → New repository secret**.
3. Crea los cuatro secretos que aparecen en el documento privado entregado al propietario:
   - `CORDERO_KEYSTORE_B64`
   - `CORDERO_STORE_PASSWORD`
   - `CORDERO_KEY_ALIAS`
   - `CORDERO_KEY_PASSWORD`
4. En **Actions → Build El Corderito APK → Run workflow**, inicia otra compilación.
5. Cuando los cuatro secretos estén presentes, el resultado se llamará `El_Corderito_v0.14-release.apk`, firmado con la identidad estable. Resguarda siempre la clave `.jks` y sus contraseñas: de lo contrario no podrás actualizar estas APKs.

**La APK debug antigua (v0.10) usa una firma diferente:** la primera instalación de la release firmada de v0.14 deberá desinstalar la debug anterior. Esto borra el almacenamiento y sesión **locales**; no elimina las cuentas, ventas ni existencias guardadas en Supabase. Desde esa primera instalación, una release futura con el **mismo applicationId y la misma clave privada** sí será instalable como actualización.

## Restricciones de seguridad

- Solo carga `https://scorderomaya-sketch.github.io/-el-corderito-app/`.
- Necesita Internet y Supabase disponible.
- No solicita cámara, ubicación ni almacenamiento; deshabilita contenidos HTTP y acceso a archivos locales.
- No incluye claves privadas, contraseñas ni credenciales privilegiadas en la APK.
- La app todavía es **beta**; valida los flujos reales antes de usarla para cobrar comercialmente.
