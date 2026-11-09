"""Demostración ficticia: no usa conexiones, clientes ni reglas reales."""

def mostrar_demo():
    ejemplo = {"contacto": "Persona de ejemplo", "organizacion": "Empresa ficticia"}
    pasos = (
        "Registro de un prospecto ficticio",
        "Verificación simulada de datos",
        "Interacción de voz NO ejecutada (simulación)",
        "Seguimiento NO enviado (simulación)",
        "Agendamiento NO solicitado (simulación)",
    )
    print("DEMOSTRACIÓN SIN CONEXIONES EXTERNAS")
    print(f"Prospecto: {ejemplo['contacto']} / {ejemplo['organizacion']}")
    for numero, paso in enumerate(pasos, start=1):
        print(f"{numero}. {paso}")

if __name__ == "__main__":
    mostrar_demo()
