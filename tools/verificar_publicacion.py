"""Guardia básica de publicación: no reemplaza una auditoría de seguridad."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RESTRICCIONES = (
    ("posible secreto", re.compile(r"(?i)\b(?:api[_-]?key|client[_-]?secret|auth[_-]?token|password)\b\s*[:=]\s*['\"][^'\"]{8,}['\"]")),
    ("token de acceso", re.compile(r"(?:gh[pousr]_[A-Za-z0-9_]{20,}|sk-(?:proj-)?[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{35})")),
    ("endpoint o dirección", re.compile(r"(?:https?://|wss?://|\b(?:\d{1,3}\.){3}\d{1,3}\b)")),
    ("clave privada", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
)
EXTENSIONES_PROHIBIDAS = {".json", ".zip", ".7z", ".pem", ".key", ".p12", ".csv", ".xlsx", ".db", ".sqlite", ".wav", ".mp3"}
NOMBRES_PROHIBIDOS = {"app.py", "credentials", "secrets"}
CARPETAS_PROHIBIDAS = {"exports", "backups", "private", "workflows", "contacts", "data", "transcripts", "call_logs", "recordings"}

def main() -> int:
    problemas = []
    for ruta in ROOT.rglob("*"):
        if not ruta.is_file():
            continue
        relativo = ruta.relative_to(ROOT)
        if any(p.startswith(".") and p not in {".github"} for p in relativo.parts[:-1]):
            continue
        if ruta.is_symlink():
            problemas.append(f"enlace simbólico no admitido: {relativo}")
            continue
        if ruta.name.lower().startswith(".env") and ruta.name != ".env.example":
            problemas.append(f"archivo de entorno restringido: {relativo}")
            continue
        if ruta.suffix.lower() in EXTENSIONES_PROHIBIDAS or ruta.name.lower() in NOMBRES_PROHIBIDOS or any(p.lower() in CARPETAS_PROHIBIDAS for p in relativo.parts[:-1] if not (p.lower() == "workflows" and relativo.parts[0] == ".github")):
            problemas.append(f"archivo restringido: {relativo}")
            continue
        if ruta.stat().st_size > 300_000:
            problemas.append(f"archivo demasiado grande para revisión pública: {relativo}")
            continue
        if ruta.suffix.lower() in {".py", ".md", ".txt", ".yml", ".yaml", ".toml"} or ruta.name == ".env.example":
            contenido = ruta.read_text(encoding="utf-8", errors="replace")
            # La propia definición de los patrones no se evalúa como contenido sensible.
            if ruta.name == "verificar_publicacion.py":
                continue
            for nombre, patron in RESTRICCIONES:
                if patron.search(contenido):
                    problemas.append(f"{nombre}: {relativo}")
    for problema in problemas:
        print(f"BLOQUEADO: {problema}")
    if problemas:
        return 1
    print("OK: no se detectaron archivos restringidos o señales básicas de secretos.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
