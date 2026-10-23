# El Corderito — APK Android beta

Aplicación Android de prueba para el sistema web El Corderito.

- **Origen web permitido:** `https://scorderomaya-sketch.github.io/-el-corderito-app/`
- **Conexión:** requiere Internet y un servidor Supabase disponible.
- **Autenticación:** correo y contraseña en el formulario de la app. Los enlaces mágicos enviados por correo se abrirán en el navegador externo, no en la sesión WebView.
- **Permisos Android:** conexión a Internet y consulta del estado de red. Sin permisos de cámara, ubicación o almacenamiento.
- **Seguridad:** bloquea HTTP en el WebView, no permite acceso a archivos locales, no añade puentes JavaScript a Android, niega permisos web sensibles.
- **Código compartido:** actualizaciones de la interfaz GitHub Pages se reflejarán al abrir o recargar la APK.
- **Beta:** el APK de depuración se firma con una clave temporal generada en GitHub Actions. Compilaciones sucesivas pueden requerir desinstalar la versión anterior para instalar la nueva, lo que elimina la sesión local. Las ventas y recetas remotas no se eliminan por ese motivo.
- **No usar para ventas reales todavía.**

## Compilar

El workflow `.github/workflows/build-android-apk.yml` instala Java 17, Gradle 8.9 y Android SDK 35 en GitHub Actions, construye el APK e incorpora el archivo firmado de depuración como artefacto.

Descárgalo desde la ejecución exitosa de **Build El Corderito APK**, sección **Artifacts**. GitHub entrega un ZIP con `El_Corderito_v0.10-beta.apk`.

La versión de producción necesitará una clave de firma Android estable, administrada fuera del repositorio público.
