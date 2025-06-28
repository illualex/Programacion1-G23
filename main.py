from gestion_productos import menu_productos
from gestion_pedidos import menu_pedidos  
from gestion_combos import menu_combos
from reportes_cbc import menu_reportes
from utils_cbc import limpiar_consola, mensaje_error

# Función principal que muestra el menú principal del sistema
def menu_principal():
    while True:
        limpiar_consola()
        print("\n[====== Menú Principal de Concordia Burger Club ======]\n")
        print("1. Gestionar Productos (Administrador)")
        print("2. Gestionar Combos (Administrador)")
        print("3. Gestionar Pedidos (Cliente)")
        print("4. Ver Reportes")
        print("5. Salir")

        opcion = input("\n Ingrese una opción: ").strip()

        # Navega a la sección correspondiente según la opción elegida
        if opcion == '1':
            menu_productos()  # Muestra menú de gestión de productos
        elif opcion == '2':
            menu_combos()     # Muestra menú de gestión de combos
        elif opcion == '3':
            menu_pedidos()    # Muestra menú de pedidos para clientes
        elif opcion == '4':
            menu_reportes()   # Muestra menú de reportes del sistema
        elif opcion == '5':
            print("Saliendo del sistema. ¡Gracias!")
            break
        else:
            mensaje_error()

# Punto de entrada principal del sistema
if __name__ == "__main__":
    menu_principal()
