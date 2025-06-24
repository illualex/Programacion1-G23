# === IMPORTS ===
from persistencia_cbc import (
    cargar_combos,
    guardar_combos,
    cargar_hamburguesas,
    cargar_acompanamientos,
    cargar_bebidas,
)
from utils_cbc import limpiar_consola, mensaje_error

# === FUNCIONES AUXILIARES ===


def elegir_producto(lista, categoria):
    """
    Muestra una lista de productos de una categoría y permite al usuario elegir uno por ID.
    Devuelve el producto elegido con la categoría incluida.
    """
    print(f"\n--- {categoria.capitalize()} disponibles ---")
    for prod in lista:
        print(f"{prod['id']}. {prod['nombre']} - ${prod['precio']}")
    while True:
        try:
            id_elegido = int(input(f"Elegí el ID de la {categoria}: "))
            for prod in lista:
                if prod["id"] == id_elegido:
                    return {**prod, "categoria": categoria}
            print("ID inválido.")
        except ValueError:
            print("Debés ingresar un número válido.")


def elegir_producto_modificable(lista, categoria, producto_actual):
    """
    Muestra productos y permite elegir uno nuevo o mantener el producto actual.
    Se usa al modificar un combo.
    """
    print(f"\n--- {categoria.capitalize()} disponibles ---")
    for prod in lista:
        print(f"{prod['id']}. {prod['nombre']} - ${prod['precio']}")
    while True:
        entrada = input(
            f"Elegí ID de {categoria} (Enter para dejar '{producto_actual['nombre']}'): "
        ).strip()
        if entrada == "":
            return producto_actual
        try:
            id_elegido = int(entrada)
            for prod in lista:
                if prod["id"] == id_elegido:
                    return {**prod, "categoria": categoria}
            print("ID inválido.")
        except ValueError:
            print("Ingresá un número válido.")


# === FUNCIONES PRINCIPALES ===


def crear_combo():
    """
    Permite crear un nuevo combo seleccionando productos de cada categoría.
    Se ingresa un nombre y un precio. El combo se guarda en combos.json.
    """
    print("\n=== Crear Nuevo Combo ===")
    hamburguesas = cargar_hamburguesas()
    acompanamientos = cargar_acompanamientos()
    bebidas = cargar_bebidas()

    if not hamburguesas or not acompanamientos or not bebidas:
        print("[ERROR] Faltan productos para crear un combo. Verificá los archivos.")
        return

    # Elegir un producto de cada categoría
    hamb = elegir_producto(hamburguesas, "hamburguesas")
    acomp = elegir_producto(acompanamientos, "acompañamientos")
    beb = elegir_producto(bebidas, "bebidas")

    # Ingresar nombre y precio del combo
    nombre = input("Ingresá el nombre del combo: ").strip()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Ingresá el nombre del combo: ").strip()

    while True:
        try:
            precio_base = float(input("Ingresá el precio del combo: "))
            if precio_base <= 0:
                raise ValueError
            break
        except ValueError:
            print("Debés ingresar un precio válido mayor a 0.")

    # Generar ID automático
    combos = cargar_combos()
    nuevo_id = max([combo["id"] for combo in combos], default=0) + 1

    # Crear y guardar combo
    nuevo_combo = {
        "id": nuevo_id,
        "nombre": nombre,
        "productos": [hamb, acomp, beb],
        "precio_base": precio_base,
    }

    combos.append(nuevo_combo)
    guardar_combos(combos)
    print(f"\n✅ Combo '{nombre}' creado con éxito.")


def modificar_combo():
    """
    Permite modificar un combo existente: cambiar nombre, productos y precio.
    Guarda los cambios en combos.json.
    """
    combos = cargar_combos()
    if not combos:
        print("\nNo hay combos para modificar.\n")
        return

    print("\n=== Modificar Combo ===")
    for combo in combos:
        print(f"{combo['id']}. {combo['nombre']}")

    # Seleccionar combo por ID
    while True:
        try:
            id_mod = int(input("Elegí el ID del combo que querés modificar: "))
            combo_sel = next((c for c in combos if c["id"] == id_mod), None)
            if combo_sel:
                break
            else:
                print("ID no encontrado. Intenta de nuevo.")
        except ValueError:
            print("Ingresá un número válido.")

    print(f"\nModificando combo: {combo_sel['nombre']}")

    # Modificar nombre
    nuevo_nombre = input(
        f"Ingresá nuevo nombre (Enter para dejar '{combo_sel['nombre']}'): "
    ).strip()
    if nuevo_nombre:
        combo_sel["nombre"] = nuevo_nombre

    # Modificar productos
    hamburguesas = cargar_hamburguesas()
    acompanamientos = cargar_acompanamientos()
    bebidas = cargar_bebidas()

    combo_sel["productos"][0] = elegir_producto_modificable(
        hamburguesas, "hamburguesas", combo_sel["productos"][0]
    )
    combo_sel["productos"][1] = elegir_producto_modificable(
        acompanamientos, "acompañamientos", combo_sel["productos"][1]
    )
    combo_sel["productos"][2] = elegir_producto_modificable(
        bebidas, "bebidas", combo_sel["productos"][2]
    )

    # Modificar precio
    while True:
        entrada = input(
            f"Ingresá nuevo precio base (Enter para dejar {combo_sel['precio_base']}): "
        ).strip()
        if entrada == "":
            break
        try:
            precio = float(entrada)
            if precio > 0:
                combo_sel["precio_base"] = precio
                break
            else:
                print("El precio debe ser mayor a 0.")
        except ValueError:
            print("Ingresá un número válido.")

    guardar_combos(combos)
    print(f"\n✅ Combo '{combo_sel['nombre']}' modificado con éxito.")


def eliminar_combo():
    """
    Permite eliminar un combo existente seleccionado por ID.
    Confirma antes de eliminar. Guarda los cambios en combos.json.
    """
    combos = cargar_combos()
    if not combos:
        print("\nNo hay combos para eliminar.\n")
        return

    print("\n=== Eliminar Combo ===")
    for combo in combos:
        print(f"{combo['id']}. {combo['nombre']}")

    # Elegir combo a eliminar
    while True:
        try:
            id_elim = int(input("Elegí el ID del combo que querés eliminar: "))
            combo_sel = next((c for c in combos if c["id"] == id_elim), None)
            if combo_sel:
                break
            else:
                print("ID no encontrado. Intenta de nuevo.")
        except ValueError:
            print("Ingresá un número válido.")

    # Confirmar eliminación
    confirmar = (
        input(
            f"¿Estás seguro que querés eliminar el combo '{combo_sel['nombre']}'? (s/n): "
        )
        .strip()
        .lower()
    )
    if confirmar == "s":
        combos = [c for c in combos if c["id"] != id_elim]
        guardar_combos(combos)
        print(f"\n✅ Combo '{combo_sel['nombre']}' eliminado con éxito.")
    else:
        print("\nOperación cancelada.")


# === MENÚ PRINCIPAL DE COMBOS ===


def menu_combos():
    """
    Muestra el menú interactivo para gestionar combos.
    Permite crear, modificar, eliminar o volver al menú anterior.
    """
    while True:
        limpiar_consola()
        print("\n===== Menú de Gestión de Combos =====")
        print("1. Crear Combo")
        print("2. Modificar Combo")
        print("3. Eliminar Combo")
        print("4. Volver al Menú Principal")

        opcion = input("\n> Ingresa una opción: ").strip()

        if opcion == "1":
            crear_combo()
        elif opcion == "2":
            modificar_combo()
        elif opcion == "3":
            eliminar_combo()
        elif opcion == "4":
            print("\n << Saliendo del menú de combos")
            input("\n Presiona Enter para continuar...")
            break
        else:
            mensaje_error()
