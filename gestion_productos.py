from persistencia_cbc import (
    cargar_hamburguesas,
    cargar_bebidas,
    cargar_acompanamientos,
    guardar_hamburguesas,
    guardar_bebidas,
    guardar_acompanamientos,
)
from utils_cbc import limpiar_consola, mensaje_error, cancelacion_rapida


# ===== FUNCIONES AUXILIARES =====
# Función para mostrar el encabezado de gestión de productos por categoría
def encabezado_gestion(nombre_categoria):
    print(f"\n[======== Gestión de {nombre_categoria.capitalize()}s ========]")


# ===== FUNCIONES PRINCIPALES =====
# Función que gestiona producto de cada categoría (hamburguesas, bebidas, acompañamientos)
def gestionar_categoria(nombre_categoria, funcion_cargar, funcion_guardar):
    productos = funcion_cargar()

    while True:
        limpiar_consola()
        encabezado_gestion(nombre_categoria)
        print("\n1. Crear un producto")
        print("2. Modificar un producto")
        print("3. Eliminar un producto")
        print("4. Volver al menú de productos")

        opcion = input("\n > Elige una opción: ").strip()

        # Sección crear producto
        if opcion == "1":
            limpiar_consola()
            encabezado_gestion(nombre_categoria)
            print(" - Salida rápida coloca 'x' -\n")
            print(" >> Crear nuevo producto <<")

            # Solicita y valida el nombre del producto
            while True:
                limpiar_consola()
                encabezado_gestion(nombre_categoria)
                print(" - Salida rápida coloca 'x' -\n")
                print(" <<--- Colocale un nombre al producto --->>")
                nombre = input("- Nombre: ").strip()
                if cancelacion_rapida(nombre):
                    return
                if not nombre:
                    print("\n >> El nombre no puede estar vacío.")
                    input("\n Presiona Enter para intentarlo de nuevo...")
                    continue
                break

            # Solicita y valida el precio del producto
            while True:
                limpiar_consola()
                encabezado_gestion(nombre_categoria)
                print(" - Salida rápida coloca 'x' -\n")
                print(" <<--- Colocale un precio al producto --->>")
                precio_input = input("- Precio: ").strip()
                if cancelacion_rapida(precio_input):
                    return
                if not precio_input:
                    print("\n >> El precio no puede estar vacío.")
                    input("\n Presiona Enter para intentarlo de nuevo...")
                    continue
                try:
                    precio = int(precio_input)
                    if precio <= 0:
                        print("\n >> El precio debe ser mayor a 0.")
                        input("\n Presiona Enter para intentarlo de nuevo...")
                        continue
                    break
                except ValueError:
                    print("\n >> Se deben ingresar números.")
                    input("\n Presiona Enter para intentarlo de nuevo...")

            # Se arma el diccionario del nuevo producto de la categoría seleccionada
            nuevo = {
                "id": max([p["id"] for p in productos], default=0) + 1,
                "nombre": nombre,
                "precio": precio,
                "categoria": nombre_categoria + "s",
            }
            productos.append(nuevo)
            funcion_guardar(productos)
            print("\n >> Producto agregado con éxito! <<")
            input("\n Presiona Enter para volver atrás...")

        # Sección modificar producto
        elif opcion == "2":
            while True:
                limpiar_consola()
                encabezado_gestion(nombre_categoria)
                print(" - Salida rápida coloca 'x' -\n")
                print("<<--- Modificar producto existente --->>")
                print(" - Productos disponibles:\n")
                for p in productos:
                    print(f"{p['id']} - {p['nombre']} - ${p['precio']}")

                id_input = input("\n > Ingrese un producto (Numero): ").strip()
                if cancelacion_rapida(id_input):
                    return

                if not id_input.isdigit():
                    mensaje_error()
                    continue

                id_mod = int(id_input)
                producto = next((p for p in productos if p["id"] == id_mod), None)
                if not producto:
                    print("\n >> El producto ingresado no existe.")
                    input("\n Presiona Enter para intentar de nuevo...")
                    continue

                # Solicita y Valida el nuevo nombre
                while True:
                    limpiar_consola()
                    encabezado_gestion(nombre_categoria)
                    print(" - Salida rápida coloca 'x' -\n")
                    print("<<--- Modifica el nombre del producto --->>")
                    print(f"- Nombre actual: {producto['nombre']}")
                    nuevo_nombre = input("\n > Nuevo nombre: ").strip()
                    if cancelacion_rapida(nuevo_nombre):
                        return
                    if not nuevo_nombre:
                        print("\n >> El nombre no puede estar vacío.")
                        input("\n Presiona Enter para intentar de nuevo...")
                        continue
                    break

                # Solicita y Valida el nuevo precio
                while True:
                    limpiar_consola()
                    encabezado_gestion(nombre_categoria)
                    print(" - Salida rápida coloca 'x' -\n")
                    print("<<--- Modifica el precio del producto --->>")
                    print(f"- Precio actual: ${producto['precio']}")
                    nuevo_precio_input = input("\n > Nuevo precio: ").strip()
                    if cancelacion_rapida(nuevo_precio_input):
                        return
                    if not nuevo_precio_input.isdigit():
                        print("\n >> Se debe ingresar números.")
                        input("\n Presiona Enter para intentarlo de nuevo...")
                        continue
                    nuevo_precio = int(nuevo_precio_input)
                    if nuevo_precio <= 0:
                        print("\n >> El precio debe ser mayor a cero.")
                        input("\n Presiona Enter para intentarlo de nuevo...")
                        continue
                    break

                # Confirmación final antes de guardar cambios
                while True:
                    limpiar_consola()
                    encabezado_gestion(nombre_categoria)
                    print("\n<<--- Confirmar modificación del producto --->>")
                    print(f"- Nombre actual : {producto['nombre']}")
                    print(f"- Precio actual : ${producto['precio']}\n")
                    print(f"> Nuevo nombre  : {nuevo_nombre}")
                    print(f"> Nuevo precio  : ${nuevo_precio}")
                    print("\n<< ¿Deseas confirmar los cambios? >>")
                    print("1. Sí, guardar modificaciones")
                    print("2. No, descartar y volver al menú")

                    opcion_conf = input("\n > Elige una opción: ").strip()
                    if opcion_conf == "1":
                        producto["nombre"] = nuevo_nombre
                        producto["precio"] = nuevo_precio
                        funcion_guardar(productos)
                        print("\n >> Producto modificado correctamente! <<")
                        input("\n Presiona Enter para volver al menú...")
                        return
                    elif opcion_conf == "2":
                        print("\n << Cambios descartados. Volviendo al menú...")
                        input("\n Presiona Enter para continuar...")
                        return
                    else:
                        mensaje_error()

        # Sección eliminar producto
        elif opcion == "3":
            while True:
                limpiar_consola()
                encabezado_gestion(nombre_categoria)
                print(" - Salida rápida coloca 'x' -\n")
                print("<<--- Eliminar un producto --->>")
                print(" - Productos disponibles:\n")
                for p in productos:
                    print(f"{p['id']} - {p['nombre']} - ${p['precio']}")

                id_input = input("\n> Ingrese un producto (Número): ").strip()
                if cancelacion_rapida(id_input):
                    return
                if not id_input.isdigit():
                    mensaje_error()
                    continue

                id_del = int(id_input)

                for p in productos:
                    if p["id"] == id_del:
                        # Confirmación antes de eliminar el producto
                        while True:
                            limpiar_consola()
                            encabezado_gestion(nombre_categoria)
                            print(
                                f"\n¿Estás seguro que deseas eliminar '{p['nombre']}'?"
                            )
                            print("1. Sí, eliminar producto")
                            print("2. No, cancelar y volver")

                            confirm = input("\n > Elige una opción: ").strip()
                            if confirm == "1":
                                productos.remove(p)
                                funcion_guardar(productos)
                                print("\n >> Producto eliminado con éxito! <<")
                                input("\n Presiona Enter para continuar...")
                                break
                            elif confirm == "2":
                                print("\n << Operación cancelada.")
                                input("\n Presiona Enter para continuar...")
                                break
                            else:
                                mensaje_error()
                        break
                else:
                    print("\n >> El producto ingresado no existe.")
                    input("\n Presiona Enter para intentar de nuevo...")
                    continue
                break

        # Sección volver al menú anterior
        elif opcion == "4":
            break
        else:
            mensaje_error()


# Función que muestra el menu de gestión de productos 
# y permite seleccionar la categoría a gestionar
def menu_productos():
    while True:
        limpiar_consola()
        print("\n[======== Menu de Gestión de Productos ========]\n")
        print(" <<--- Seleccione una categoría --->>")
        print("1. Gestionar hamburguesas")
        print("2. Gestionar bebidas")
        print("3. Gestionar acompañamientos")
        print("4. Volver al menú principal")

        opcion = input("\n > Ingrese una opción: ").strip()

        if opcion == "1":
            gestionar_categoria(
                "hamburguesa", cargar_hamburguesas, guardar_hamburguesas
            )
        elif opcion == "2":
            gestionar_categoria("bebida", cargar_bebidas, guardar_bebidas)
        elif opcion == "3":
            gestionar_categoria(
                "acompañamiento", cargar_acompanamientos, guardar_acompanamientos
            )
        elif opcion == "4":
            print("\n << Volviendo al menú principal...")
            input("\n Presiona Enter para continuar...")
            break
        else:
            mensaje_error()


# Iniciar el programa sin pasar por el main.py
if __name__ == "__main__":
    menu_productos()
