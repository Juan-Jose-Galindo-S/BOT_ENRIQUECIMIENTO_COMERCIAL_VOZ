# Arquitectura pública (conceptual)

```mermaid
flowchart TD
    A[Fuente autorizada de prospectos] --> B[Preparación y calidad de datos]
    B --> C[Orquestación comercial]
    C --> D[Interacción asistida por voz]
    D --> E[Seguimiento y resultados]
    E --> F[Agendamiento autorizado]
    C -.-> G[Controles de consentimiento y auditoría]
    D -.-> G
    E -.-> G
```

**No es un diagrama de implementación.** Se omitieron intencionalmente proveedores, endpoints, modelos, reglas de negocio, prompts, credenciales y protocolos internos.

## Principios

1. Separación entre interfaces, datos y operación.
2. Procesamiento limitado a contactos y datos con autorización aplicable.
3. Credenciales fuera del código y de la documentación pública.
4. Seguimiento auditable con acceso y retención definidos.
