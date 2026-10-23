# El Corderito — aplicación beta

Panel de ventas, inventario y administración para El Corderito. Esta versión es un prototipo web conectado a Supabase y **no debe usarse todavía con ventas reales**.

## Publicar GitHub Pages

1. Entrar en **Settings → Pages** de este repositorio.
2. En **Build and deployment → Source**, elegir **Deploy from a branch**.
3. Elegir la rama **main** y carpeta **/(root)**, y guardar.
4. URL esperada cuando GitHub termine de publicar: https://scorderomaya-sketch.github.io/-el-corderito-app/

## Configurar inicio de sesión

En Supabase, **Authentication → URL Configuration**:
- **Site URL**: `https://scorderomaya-sketch.github.io/-el-corderito-app/`
- **Redirect URLs**: incluir exactamente `https://scorderomaya-sketch.github.io/-el-corderito-app/`

Panel de Supabase: https://supabase.com/dashboard/project/xqdzpdbdvevqspshgxzk/auth/url-configuration

## Seguridad y limitaciones

- No guardar contraseñas, enlaces de inicio de sesión ni claves secretas en este repositorio público.
- El frontend contiene únicamente la clave *publishable* de Supabase; la autorización real se aplica mediante RLS y funciones del servidor.
- La aplicación aún no permite modificar recetas ni lotes en la nube; faltan pruebas con varias cuentas, corte de caja completo y APK.
- Los importes cargados inicialmente son ejemplos y la venta requiere inventario/consumo configurados.
