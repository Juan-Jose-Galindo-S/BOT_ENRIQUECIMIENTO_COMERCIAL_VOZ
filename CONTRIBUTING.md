# Contribuciones

Este repositorio es una **edición pública de presentación**, no un proyecto de código abierto. Se aceptan propuestas de mejora de documentación y de la simulación, sujetas a revisión del responsable.

## Proceso

1. Abre una incidencia sin incluir información interna, comercial o personal.
2. Propón cambios acotados en una rama independiente.
3. Ejecuta antes de solicitar revisión:

   ```bash
   python tools/verificar_publicacion.py
   python -m unittest discover -s tests -v
   python demo/simulacion.py
   ```

4. Comprueba el contenido de los cambios y del historial. No incorpores archivos originales ni configuraciones operativas.

## Uso y derechos

El material se publica con **todos los derechos reservados**. La posibilidad técnica de abrir una propuesta no concede permisos de explotación, redistribución o uso de las partes del proyecto. No se reciben contribuciones que requieran divulgar lógica propietaria.
