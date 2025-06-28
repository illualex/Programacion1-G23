import os


# Función para limpiar la consola
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


# Funcion para mostrar un mensaje de error estándar
def mensaje_error():
    print("\n >> Opción inválida.")
    input("\n Presiona Enter para intentar de nuevo...")


# Funcion para cancelar una operación rápida
def cancelacion_rapida(entrada):
    if entrada.strip().lower() == "x":
        print("\n << Operación cancelada. Volviendo al menú...")
        input("\n Presiona Enter para continuar...")
        return True
    return False
