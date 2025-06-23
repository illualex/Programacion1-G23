import os

# === Función para limpiar la consola ===
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# === Mensaje de error ===
def mensaje_error():
    print("\n >> Opción inválida.")
    input("\n Presiona Enter para intentar de nuevo...")