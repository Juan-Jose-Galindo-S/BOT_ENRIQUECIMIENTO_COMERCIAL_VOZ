# BOT_ENRIQUECIMIENTO_COMERCIAL_VOZ

**Plataforma de automatización comercial asistida por inteligencia artificial.**

Proyecto orientado a mejorar los procesos de prospección mediante la organización y el enriquecimiento de información comercial, la gestión de interacciones de voz y el seguimiento de oportunidades.

## Capacidades generales

- Organización y enriquecimiento de información de prospectos.
- Coordinación de campañas y seguimiento comercial.
- Interacciones de voz asistidas por inteligencia artificial.
- Registro de estados y resultados de contacto.
- Apoyo al agendamiento y a las confirmaciones comerciales.
- Controles de autorización, privacidad y trazabilidad.

## Alcance de esta edición pública

Este repositorio contiene **documentación de alto nivel y una simulación local no operativa**. No incluye el motor de voz, reglas de segmentación, prompts de producción, conectores, flujos de automatización, credenciales, URLs internas ni configuraciones de clientes.

**No es un despliegue funcional**. La versión operativa y sus integraciones se mantienen fuera de este repositorio.

## Demostración local opcional

Requiere Python 3.10 o superior; no necesita paquetes externos ni acceso a internet.

```bash
python demo/simulacion.py
```

La simulación usa datos inventados, sin hacer llamadas telefónicas, conexiones externas, enriquecimiento real ni reservas.

## Estructura

- `docs/ARQUITECTURA_PUBLICA.md`: componentes funcionales a nivel conceptual.
- `docs/POLITICA_PUBLICACION.md`: reglas para no revelar material sensible.
- `demo/simulacion.py`: demostración completamente ficticia.
- `SECURITY.md`: prácticas de seguridad y canal de reporte.
- `tools/verificar_publicacion.py`: comprobaciones locales para evitar cargas accidentales.
- `tests/test_publicacion.py`: pruebas de la política de publicación.
- `CONTRIBUTING.md`: requisitos para propuestas de cambio.

## Verificación local

```bash
python tools/verificar_publicacion.py
python -m unittest discover -s tests -v
python demo/simulacion.py
```

La revisión es preventiva y **no garantiza** que un cambio esté libre de secretos o vulnerabilidades. Debe complementarse con una revisión humana antes de publicar.

## Propiedad intelectual

© 2026. Todos los derechos reservados. No se otorga una licencia de software para usar, modificar, redistribuir ni explotar comercialmente el contenido. La ausencia de una licencia no impide que el contenido público pueda ser visualizado; el código privado debe mantenerse en un repositorio de acceso restringido.
