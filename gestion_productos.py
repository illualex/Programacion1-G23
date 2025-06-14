from persistencia_cbc import cargar_productos, guardar_productos

def menu_productos():
    productos = cargar_productos()
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Listar productos")
        print("2. Agregar producto")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Volver")
        opcion = input("Opción: ")

        if opcion == '1':
            for p in productos:
                print(f"ID: {p['id']} - {p['nombre']} (${p['precio']}) - {p['categoria']}")
        elif opcion == '2':
            nombre = input("Nombre: ")
            precio = int(input("Precio: "))
            categoria = input("Categoría: ")
            nuevo = {"id": len(productos)+1, "nombre": nombre, "precio": precio, "categoria": categoria}
            productos.append(nuevo)
            guardar_productos(productos)
        elif opcion == '3':
            id_mod = int(input("ID a modificar: "))
            for p in productos:
                if p['id'] == id_mod:
                    p['nombre'] = input("Nuevo nombre: ")
                    p['precio'] = int(input("Nuevo precio: "))
                    p['categoria'] = input("Nueva categoría: ")
                    guardar_productos(productos)
                    break
        elif opcion == '4':
            id_del = int(input("ID a eliminar: "))
            productos = [p for p in productos if p['id'] != id_del]
            guardar_productos(productos)
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")
