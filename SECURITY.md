# Política de seguridad

Esta edición pública es **una vista conceptual**, no un backend ni un sistema productivo.

No abras incidencias públicas con secretos, grabaciones, datos personales, tokens, capturas de clientes o enlaces privados. Usa un canal de contacto privado con la persona responsable del proyecto.

## Requisitos de la edición productiva (no incluida)

- Secretos en un gestor de secretos o variables seguras, nunca dentro de archivos versionados.
- Autenticación verificable y permisos mínimos para cada webhook y servicio.
- Restricciones de red y HTTPS/WSS para integraciones.
- Protección contra abuso mediante límites, auditoría y controles de autorización.
- Separación de ambientes y rotación de credenciales ante cualquier filtración.
- Minimización, acceso restringido y retención limitada de datos personales.
- Autorización verificable antes de realizar contactos automatizados.
- Revisión de dependencias, escaneo de secretos y controles antes de cada publicación.

Los secretos incluidos alguna vez en un commit deben **revocarse o rotarse**, incluso si el archivo se elimina después. `.gitignore` no elimina el historial.
