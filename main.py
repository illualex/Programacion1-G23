from gestion_productos import menu_productos
from gestion_pedidos import menu_pedidos  
from reportes_cbc import menu_reportes
from utils_cbc import limpiar_consola


def menu_principal():
    while True:
        limpiar_consola()
        print("\n ===== Gestión Concordia Burger Club =====")
        print("1. Gestionar Productos [Administrador]")
        print("2. Gestionar Pedidos [Cliente]")
        print("3. Ver Reportes")
        print("4. Salir")
        opcion = input("\n Elegí una opción: ")

        if opcion == '1':
            menu_productos()
        elif opcion == '2':
            menu_pedidos()
        elif opcion == '3':
            menu_reportes()
        elif opcion == '4':
            print("Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()