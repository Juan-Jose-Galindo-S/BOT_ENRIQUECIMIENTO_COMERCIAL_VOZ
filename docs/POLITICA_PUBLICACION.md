# Lista de control para publicación

## Nunca incluir en este repositorio

- Exports de workflows, configuraciones de agentes o pipelines reales.
- Código del motor de llamadas, instrucciones del modelo o lógica comercial propietaria.
- Tokens, contraseñas, headers de autenticación, OAuth, identificadores de credenciales.
- URLs de producción, rutas privadas, IP, IDs de documentos y detalles de infraestructura.
- Bases de datos, contactos, registros de llamadas, transcripciones, correos o números reales.
- Copias de seguridad, archivos comprimidos del proyecto original ni documentación interna.

## Antes de cada push

1. Revisar cada archivo nuevo y ejecutar `python tools/verificar_publicacion.py`.
2. Verificar con `git status` y `git diff --cached` el contenido exacto que será enviado.
3. Confirmar que no se incluye historial de otro repositorio; crear un historial nuevo para la edición pública.
4. Habilitar en GitHub las alertas y protección de secretos disponibles para el repositorio.
5. Mantener el código funcional en un repositorio **privado** separado.

Si un secreto ya se compartió, retirarlo de la publicación **no es suficiente**: rotarlo o revocarlo en el proveedor y revisar registros de acceso.

La documentación pública muestra qué problema aborda el proyecto, no cómo replicar la implementación privada.
