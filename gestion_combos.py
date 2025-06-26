from persistencia_cbc import (
    cargar_combos,
    guardar_combos,
    cargar_hamburguesas,
    cargar_acompanamientos,
    cargar_bebidas,
)
from utils_cbc import limpiar_consola, mensaje_error, cancelacion_rapida


# === FUNCIONES AUXILIARES ===
# === Encabezado para crear un nuevo combo ===
def encabezado_combos():
    print("\n======== Crear Nuevo Combo ========")
    print(" - Salida rápida coloca 'x' -\n")


# === Encabezado para modificar un combo ===
def encabezado_modificar_combo():
    print("\n======== Modificar Combo ========")
    print(" - Salida rápida coloca 'x' -\n")


# === Función para elegir un producto de una categoría ===
def elegir_producto(lista, categoria):
    while True:
        limpiar_consola()
        encabezado_combos()
        print(f" <<--- {categoria.capitalize()} disponibles --->>")
        for prod in lista:
            print(f"{prod['id']}. {prod['nombre']} - ${prod['precio']}")

        entrada = input(f"\n > Elige un producto de {categoria}: ").strip()

        # Cancelación rápida
        if cancelacion_rapida(entrada):
            return False

        try:
            id_elegido = int(entrada)
            for prod in lista:
                if prod["id"] == id_elegido:
                    return {**prod, "categoria": categoria}
            print("\n >> Producto no encontrado.")
            input("\n Presiona Enter para intentar de nuevo...")
        except ValueError:
            mensaje_error()


# === Mostrar selección actual del combo ===
def mostrar_seleccion_combo(hamb, acomp, beb, nombre=None, precio_base=None):
    print(" <<--- Productos para el combo --->>")
    print("> Selección:")
    print(f"- {hamb['nombre']} - ${hamb['precio']}")
    print(f"- {acomp['nombre']} - ${acomp['precio']}")
    print(f"- {beb['nombre']} - ${beb['precio']}")

    if nombre is not None:
        print(f"\n- Nombre: {nombre}")
    if precio_base is not None:
        print(f"- Precio: $ {precio_base}")


# === FUNCIONES PRINCIPALES ===
# === Crear Combo ===
def crear_combo():
    limpiar_consola()
    encabezado_combos()

    # Cargar productos de cada categoría
    hamburguesas = cargar_hamburguesas()
    acompanamientos = cargar_acompanamientos()
    bebidas = cargar_bebidas()

    if not hamburguesas or not acompanamientos or not bebidas:
        print(
            "\n > [ERROR] Faltan productos para crear un combo. Verifica los archivos."
        )
        input("\n Presiona Enter para volver al menú...")
        return

    # Elegir un producto de cada categoría
    hamb = elegir_producto(hamburguesas, "hamburguesas")
    if hamb is False:
        return

    acomp = elegir_producto(acompanamientos, "acompañamientos")
    if acomp is False:
        return

    beb = elegir_producto(bebidas, "bebidas")
    if beb is False:
        return

    # Ingresar nombre del combo
    while True:
        limpiar_consola()
        encabezado_combos()
        mostrar_seleccion_combo(hamb, acomp, beb)  # Sin nombre ni precio aún

        nombre = input("\n > Ingresa el nombre del combo: ").strip()
        if cancelacion_rapida(nombre):
            return
        if not nombre:
            print("\n > El nombre no puede estar vacío.")
            input("\n Presiona Enter para intentar de nuevo...")
        else:
            break

    # Ingresar precio base
    while True:
        limpiar_consola()
        encabezado_combos()
        mostrar_seleccion_combo(
            hamb, acomp, beb, nombre=nombre
        )  # Mostrar con nombre pero sin precio

        entrada = input("\n > Ingresa el precio del combo: ").strip()
        if cancelacion_rapida(entrada):
            return
        try:
            precio_base = int(entrada)
            if precio_base <= 0:
                print("\n > El precio debe ser mayor a 0")
                input("\n Presiona Enter para intentar de nuevo...")
            else:
                break
        except ValueError:
            mensaje_error()

    # Confirmar creación del combo
    while True:
        limpiar_consola()
        encabezado_combos()
        mostrar_seleccion_combo(hamb, acomp, beb, nombre, precio_base)

        print("\n------------------------------")
        print(">> ¿Deseas crear este combo? <<")
        print("1. Sí.")
        print("2. No, volver al menú de combos.\n")

        opcion_confirmacion = input("> Elige una opción: ").strip()
        if opcion_confirmacion == "1":
            combos = cargar_combos()
            nuevo_id = max([combo["id"] for combo in combos], default=0) + 1

            nuevo_combo = {
                "id": nuevo_id,
                "nombre": nombre,
                "productos": [hamb, acomp, beb],
                "precio_base": precio_base,
            }

            combos.append(nuevo_combo)
            guardar_combos(combos)

            print(f"\n << El Combo '{nombre}' creado con éxito >>")
            input("\n Presiona Enter para volver al menú de combos...")
            break

        elif opcion_confirmacion == "2":
            print("\n << Operación cancelada. Volviendo al menú de combos...")
            input("\n Presiona Enter para continuar...")
            break
        else:
            mensaje_error()


# === Modificar Combo ===
def modificar_combo():
    combos = cargar_combos()
    if not combos:
        print("\n > No hay combos para modificar.")
        input("\n Presiona Enter para volver al menú...")
        return

    # Elegir el combo a modificar
    while True:
        limpiar_consola()
        encabezado_modificar_combo()
        print("<--- Seleccione un combo --->")
        for combo in combos:
            print(f"{combo['id']}. {combo['nombre']}")

        entrada = input("\n > Elige un Combo: ").strip()
        if cancelacion_rapida(entrada):
            return
        try:
            id_mod = int(entrada)
            combo_sel = next((c for c in combos if c["id"] == id_mod), None)
            if combo_sel:
                break
            print("\n >> Combo no encontrado.")
            input("\n Presiona Enter para intentar de nuevo...")
        except ValueError:
            mensaje_error()

    # Modificar nombre
    while True:
        limpiar_consola()
        encabezado_modificar_combo()
        print(">> Nuevo nombre del combo <<")
        print(f"- Nombre Actual: {combo_sel['nombre']}")
        nuevo_nombre = input(f"\n > Ingrese el nuevo nombre: ").strip()

        if cancelacion_rapida(nuevo_nombre):
            return

        if nuevo_nombre:
            combo_sel["nombre"] = nuevo_nombre
            limpiar_consola()
            break  # Solo se rompe el bucle si el nombre es válido
        else:
            print("\n >> El nombre no puede estar vacío.")
            input("\n Presiona Enter para intentar de nuevo...")

    # Modificar precio
    while True:
        limpiar_consola()
        encabezado_modificar_combo()
        print(">> Nuevo precio del Combo <<")
        print(f"- Precio Actual: ${combo_sel['precio_base']}")

        entrada = input("\n > Ingrese el nuevo precio: ").strip()

        if cancelacion_rapida(entrada):
            return

        if not entrada:
            print("\n >> El precio no puede estar vacío.")
            input("\n Presiona Enter para intentar de nuevo...")
            continue

        if not entrada.isdigit():
            mensaje_error()
            continue

        precio = int(entrada)
        if precio <= 0:
            print("\n >> El precio debe ser mayor a 0")
            input("\n Presiona Enter para intentar de nuevo...")
            continue

        # Si pasó todas las validaciones, se actualiza el precio
        combo_sel["precio_base"] = precio
        break

    # Confirmar cambios
    while True:
        limpiar_consola()
        encabezado_modificar_combo()
        print(">> Combo modificado <<")
        print(f"- Nombre: {combo_sel['nombre']}")
        print("- Productos:")
        for prod in combo_sel["productos"]:
            print(f"  • {prod['nombre']} - ${prod['precio']}")
        print(f"- Precio base: ${combo_sel['precio_base']}")
        print("\n-----------------------------")
        print("¿Deseás guardar los cambios?")
        print("1. Sí, guardar")
        print("2. No, cancelar y volver al menú\n")

        opcion = input("> Elegí una opción: ").strip()
        if opcion == "1":
            guardar_combos(combos)
            print(f"\n >> El Combo '{combo_sel['nombre']}' fue modificado con éxito.")
            input("\n Presiona Enter para volver al menú...")
            return
        elif opcion == "2":
            print("\n << Cambios descartados. Volviendo al menú...")
            input("\n Presiona Enter para continuar...")
            return
        else:
            mensaje_error()


# === Eliminar Combo ===
# === Eliminar Combo ===
def eliminar_combo():
    combos = cargar_combos()
    if not combos:
        print("\nNo hay combos para eliminar.")
        input("\nPresiona Enter para volver al menú...")
        return

    while True:
        limpiar_consola()
        print("======== Eliminar Combo ========")
        print(" - Salida rápida coloca 'x' -\n")

        print(">> Combos disponibles <<")
        for combo in combos:
            print(f"{combo['id']}. {combo['nombre']}")

        entrada = input("\n > Elige el combo a eliminar: ").strip()
        if cancelacion_rapida(entrada):
            return
        if not entrada.isdigit():
            mensaje_error()
            continue

        id_elim = int(entrada)
        combo_sel = next((c for c in combos if c["id"] == id_elim), None)
        if not combo_sel:
            print("\n >> Combo no encontrado.")
            input("\n Presiona Enter para intentar de nuevo...")
            continue

        # Confirmación
        while True:
            limpiar_consola()
            print("======== Eliminar Combo ========")
            print(" - Salida rápida coloca 'x' -\n")
            print(f"> Seleccionaste: {combo_sel['nombre']}")
            print("\n>> ¿Estás seguro que querés eliminar este combo? <<")
            print("1. Sí, eliminar.")
            print("2. No, volver al menú de combos.")

            opcion = input("\n > Elige una opción: ").strip()

            if opcion == "1":
                combos = [c for c in combos if c["id"] != id_elim]
                guardar_combos(combos)
                print(f"\n >> Combo '{combo_sel['nombre']}' eliminado con éxito.")
                input("\n Presiona Enter para volver al menú...")
                return

            elif opcion == "2":
                print("\n << Operación cancelada. Volviendo al menú de combos...")
                input("\n Presiona Enter para continuar...")
                return

            else:
                mensaje_error()


# === Menu de combos ===
def menu_combos():
    while True:
        limpiar_consola()
        print("\n[======== Menú de Gestión de Combos =======]\n")
        print("1. Crear Combo")
        print("2. Modificar Combo")
        print("3. Eliminar Combo")
        print("4. Volver al Menú Principal")

        opcion = input("\n> Ingrese una opción: ").strip()

        if opcion == "1":
            crear_combo()
        elif opcion == "2":
            modificar_combo()
        elif opcion == "3":
            eliminar_combo()
        elif opcion == "4":
            print("\n << Saliendo del menú de Combos")
            input("\n Presiona Enter para continuar...")
            break
        else:
            mensaje_error()
