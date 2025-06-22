from persistencia_cbc import (
    cargar_hamburguesas,
    cargar_bebidas,
    cargar_acompanamientos,
    guardar_hamburguesas,
    guardar_bebidas,
    guardar_acompanamientos
)

def menu_productos():
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Gestionar hamburguesas")
        print("2. Gestionar bebidas")
        print("3. Gestionar acompañamientos")
        print("4 . gestionar combos")
        print("5. Volver")
        opcion = input("Opción: ")

        if opcion == '1':
            gestionar_categoria("hamburguesa", cargar_hamburguesas, guardar_hamburguesas)
        elif opcion == '2':
            gestionar_categoria("bebida", cargar_bebidas, guardar_bebidas)
        elif opcion == '3':
            gestionar_categoria("acompañamiento", cargar_acompanamientos, guardar_acompanamientos)
        elif opcion == '4':
            break
        else:
            print("❌ Opción inválida.")

def gestionar_categoria(nombre_categoria, funcion_cargar, funcion_guardar):
    productos = funcion_cargar()

    while True:
        print(f"\n--- {nombre_categoria.capitalize()}s ---")
        print("1. Listar")
        print("2. Agregar")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Volver")
        opcion = input("Opción: ")

        if opcion == '1':
            for p in productos:
                print(f"ID: {p['id']} - {p['nombre']} (${p['precio']})")
        elif opcion == '2':
            nombre = input("Nombre: ")
            precio = int(input("Precio: "))
            nuevo = {
                "id": max([p["id"] for p in productos], default=0) + 1,
                "nombre": nombre,
                "precio": precio,
                "categoria": nombre_categoria + "s"  # para mantener compatibilidad con lógica anterior
            }
            productos.append(nuevo)
            funcion_guardar(productos)
        elif opcion == '3':
            id_mod = int(input("ID a modificar: "))
            for p in productos:
                if p['id'] == id_mod:
                    p['nombre'] = input("Nuevo nombre: ")
                    p['precio'] = int(input("Nuevo precio: "))
                    funcion_guardar(productos)
                    break
        elif opcion == '4':
            id_del = int(input("ID a eliminar: "))
            productos = [p for p in productos if p['id'] != id_del]
            funcion_guardar(productos)
        elif opcion == '5':
            break
        else:
            print("❌ Opción inválida.")
