from gestion_productos import menu_productos
from gestion_pedidos import menu_pedidos  
from gestion_combos import menu_combos
from reportes_cbc import menu_reportes
from utils_cbc import limpiar_consola, mensaje_error


def menu_principal():
    while True:
        limpiar_consola()
        print("\n[====== Gestión Principal de Concordia Burger Club ======]\n")
        print("1. Gestionar Productos (Administrador)")
        print("2. Gestionar Combos (Administrador)")
        print("3. Gestionar Pedidos (Cliente)")
        print("4. Ver Reportes")
        print("5. Salir")
        opcion = input("\n Ingrese una opción: ").strip()

        if opcion == '1':
            menu_productos()
        elif opcion == '2':
            menu_combos()
        elif opcion == '3':
            menu_pedidos()
        elif opcion == '4':
            menu_reportes()
        elif opcion == '5':
            print("Saliendo del sistema. ¡Gracias!")
            break
        else:
            mensaje_error()


if __name__ == "__main__":
    menu_principal()
