"""Pruebas sin dependencias para la guardia de publicación."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

from tools import verificar_publicacion


class VerificacionPublicacionTests(TestCase):
    def verificar(self, nombre: str, contenido: str) -> int:
        with TemporaryDirectory() as temporal:
            raiz = Path(temporal)
            archivo = raiz / nombre
            archivo.parent.mkdir(parents=True, exist_ok=True)
            archivo.write_text(contenido, encoding="utf-8")
            with patch.object(verificar_publicacion, "ROOT", raiz):
                with redirect_stdout(StringIO()):
                    return verificar_publicacion.main()

    def test_archivo_publico(self):
        self.assertEqual(self.verificar("documentacion.md", "Ejemplo ficticio."), 0)

    def test_exportacion_json_prohibida(self):
        self.assertEqual(self.verificar("exportacion.json", "{}"), 1)

    def test_entorno_local_prohibido(self):
        self.assertEqual(self.verificar(".env.production", "MODO=privado"), 1)

    def test_endpoint_externo_prohibido(self):
        direccion = "ht" + "tps://ejemplo.invalid"
        self.assertEqual(self.verificar("docs/nota.md", direccion), 1)

    def test_directorio_privado_prohibido(self):
        self.assertEqual(self.verificar("private/nota.md", "No publicar"), 1)
