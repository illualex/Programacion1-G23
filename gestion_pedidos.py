import random
from datetime import datetime
from persistencia_cbc import (
    cargar_pedidos,
    guardar_pedidos,
    cargar_hamburguesas,
    cargar_bebidas,
    cargar_acompanamientos,
    cargar_combos,
)
from utils_cbc import limpiar_consola, mensaje_error, cancelacion_rapida

# ====== CONSTANTES GLOBALES ======
# Límites y recargos utilizados en la personalización del pedido
LIMITE_ADEREZOS_SIN_RECARGO = 5
RECARGO_ADEREZOS = 100

RECARGO_BEBIDA_MEDIANA = 300
RECARGO_BEBIDA_GRANDE = 500

RECARGO_ACOMPANAMIENTO_MEDIANAS = 400
RECARGO_ACOMPANAMIENTO_GRANDES = 600

RECARGO_HAMBURGUESA_MEDIANA = 600
RECARGO_HAMBURGUESA_GRANDE = 1000

# ====== FUNCIONES AUXILIARES ======
# Función que genera un número de ticket aleatorio de 5 dígitos
def generar_numero_ticket():
    return random.randint(10000, 99999)

# Función que muestra el encabezado del pedido
def encabezado_pedido():
    print("\n[======== Armado de Pedido ========]")
    print(" - Salida rápida coloca 'x' -\n")

# Función que maneja la personalización del pedido (tamaños de productos)
def personalizacion_pedido(pedido):
    while True:
        limpiar_consola()
        encabezado_pedido()
        print(" <<--- ¿Quieres agrandar el pedido? --->>")
        print("1. Sí")
        print("2. No")
        entrada = input("\n > Elige una opción: ").strip()
        if cancelacion_rapida(entrada):
            return False
        if entrada == "2":
            return True
        elif entrada == "1":

            # Tamaño Bebida
            while True:
                limpiar_consola()
                encabezado_pedido()
                print(" <<--- Elige el tamaño de la bebida --->>")
                print("1. Chica [Por defecto]")
                print(f"2. Mediana (+${RECARGO_BEBIDA_MEDIANA})")
                print(f"3. Grande (+${RECARGO_BEBIDA_GRANDE})")
                entrada = input("\n > Elige una opción: ").strip()
                if cancelacion_rapida(entrada):
                    return False
                if entrada == "2":
                    pedido["total"] += RECARGO_BEBIDA_MEDIANA
                    pedido["tamaño_bebida"] = "mediano"
                    pedido["recargo_tamaño_bebida"] = RECARGO_BEBIDA_MEDIANA
                    break
                elif entrada == "3":
                    pedido["total"] += RECARGO_BEBIDA_GRANDE
                    pedido["tamaño_bebida"] = "grande"
                    pedido["recargo_tamaño_bebida"] = RECARGO_BEBIDA_GRANDE
                    break
                elif entrada == "1":
                    pedido["tamaño_bebida"] = "chica"
                    pedido["recargo_tamaño_bebida"] = 0
                    break
                else:
                    mensaje_error()

            # Tamaño Acompañamiento
            while True:
                limpiar_consola()
                encabezado_pedido()
                print(" <<--- Elige el tamaño del acompañamiento --->>")
                print("1. Chica [Por defecto]")
                print(f"2. Mediana (+${RECARGO_ACOMPANAMIENTO_MEDIANAS})")
                print(f"3. Grande (+${RECARGO_ACOMPANAMIENTO_GRANDES})")
                entrada = input("\n > Elige una opción: ").strip()
                if cancelacion_rapida(entrada):
                    return False
                if entrada == "2":
                    pedido["total"] += RECARGO_ACOMPANAMIENTO_MEDIANAS
                    pedido["tamaño_papas"] = "mediano"
                    pedido["recargo_tamaño_papas"] = RECARGO_ACOMPANAMIENTO_MEDIANAS
                    break
                elif entrada == "3":
                    pedido["total"] += RECARGO_ACOMPANAMIENTO_GRANDES
                    pedido["tamaño_papas"] = "grande"
                    pedido["recargo_tamaño_papas"] = RECARGO_ACOMPANAMIENTO_GRANDES
                    break
                elif entrada == "1":
                    pedido["tamaño_papas"] = "chica"
                    pedido["recargo_tamaño_papas"] = 0
                    break
                else:
                    mensaje_error()

            # Tamaño Hamburguesa
            while True:
                limpiar_consola()
                encabezado_pedido()
                print(" <<--- Elige el tamaño de la hamburguesa --->>")
                print("1. Chica [Por defecto]")
                print(f"2. Mediana (+${RECARGO_HAMBURGUESA_MEDIANA})")
                print(f"3. Grande (+${RECARGO_HAMBURGUESA_GRANDE})")
                entrada = input("\n > Elige una opción: ").strip()
                if cancelacion_rapida(entrada):
                    return False
                if entrada == "2":
                    pedido["total"] += RECARGO_HAMBURGUESA_MEDIANA
                    pedido["tamaño_hamburguesa"] = "mediana"
                    pedido["recargo_tamaño_hamburguesa"] = RECARGO_HAMBURGUESA_MEDIANA
                    break
                elif entrada == "3":
                    pedido["total"] += RECARGO_HAMBURGUESA_GRANDE
                    pedido["tamaño_hamburguesa"] = "grande"
                    pedido["recargo_tamaño_hamburguesa"] = RECARGO_HAMBURGUESA_GRANDE
                    break
                elif entrada == "1":
                    pedido["tamaño_hamburguesa"] = "chica"
                    pedido["recargo_tamaño_hamburguesa"] = 0
                    break
                else:
                    mensaje_error()

            return True
        else:
            mensaje_error()

# Función que muestra un resumen del pedido antes de confirmarlo
def resumen_pedido(pedido):
    while True:
        limpiar_consola()
        encabezado_pedido()
        print(" <<---- Resumen del Pedido ---->>")
        print(f"Cliente: {pedido['cliente']}")

        # Mostrar combo si se eligió
        if pedido.get("combo"):
            print(f"\nCombo: {pedido['combo']}")

        # Mostrar los productos elegidos
        print("\nProductos:")
        for prod in pedido["productos"]:
            if isinstance(prod, dict):
                print(f"- {prod['nombre']}: ${prod['precio']}")
            else:
                print(f"- {prod}")

        # Mostrar aderezos si se agregaron
        if pedido["cantidad_aderezos"] > 0:
            print(f"\nAderezos: {pedido['cantidad_aderezos']}")
            if pedido.get("recargo_aderezos", 0) > 0:
                print(f"Recargo por exceso de aderezos: ${pedido['recargo_aderezos']}")

        # Mostrar personalizaciones (si hay)
        personalizaciones = []
        if pedido.get("tamaño_bebida"):
            recargo = pedido.get("recargo_tamaño_bebida", 0)
            texto = f"- Tamaño de bebida: {pedido['tamaño_bebida']}"
            if recargo > 0:
                texto += f" (+${recargo})"
            personalizaciones.append(texto)

        if pedido.get("tamaño_papas"):
            recargo = pedido.get("recargo_tamaño_papas", 0)
            texto = f"- Tamaño de papas: {pedido['tamaño_papas']}"
            if recargo > 0:
                texto += f" (+${recargo})"
            personalizaciones.append(texto)

        if pedido.get("tamaño_hamburguesa"):
            recargo = pedido.get("recargo_tamaño_hamburguesa", 0)
            texto = f"- Tamaño de hamburguesa: {pedido['tamaño_hamburguesa']}"
            if recargo > 0:
                texto += f" (+${recargo})"
            personalizaciones.append(texto)

        if personalizaciones:
            print("\nPersonalización:")
            for item in personalizaciones:
                print(item)

        print(f"\nTotal a pagar: ${pedido['total']}")

        # Confirmación del pedido
        print("\n----------------------------------\n")
        print(" >>> ¿Deseas confirmar este pedido? <<<")
        print("1. Confirmar y guardar")
        print("2. Cancelar")
        eleccion = input("\n > Elige una opción: ").strip()

        if eleccion == "1":
            return True
        elif eleccion == "2":
            print("\n << Pedido cancelado.")
            input("\n Presiona Enter para volver al menú de pedidos...")
            return False
        else:
            mensaje_error()


# ====== FUNCIONES PRINCIPALES ======
# Función que permite crear un pedido a partir de productos y combos disponibles.
def crear_pedido(pedidos, combos):
    while True:
        # Se arma el diccionario del pedido
        pedido = {
            "id": len(pedidos) + 1,
            "combo": None,
            "productos": [],
            "tamaño_bebida": None,
            "recargo_tamaño_bebida": 0,
            "tamaño_papas": None,
            "recargo_tamaño_papas": 0,
            "tamaño_hamburguesa": None,
            "recargo_tamaño_hamburguesa": 0,
            "cantidad_aderezos": 0,
            "recargo_aderezos": 0,
            "total": 0,
            "cliente": "",
            "numero_ticket": generar_numero_ticket(),
            "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        # Se pregunta si desea armar el pedido o elegir un combo
        while True:
            limpiar_consola()
            encabezado_pedido()
            print(" <<--- ¿Qué quieres ordenar? --->>")
            print("1. Armar tu pedido")
            print("2. Elegir un combo")
            opcion = input("\n > Elige una opción: ").strip()
            if cancelacion_rapida(opcion):
                return
            if opcion in ["1", "2"]:
                break
            mensaje_error()

        # Apartado para elegir un combo
        if opcion == "2":
            while True:
                limpiar_consola()
                encabezado_pedido()
                print(" <<--- Combos disponibles --->>")
                # Se listan los combos disponibles
                for combo in combos:
                    print(f"{combo['id']}. {combo['nombre']}: ${combo['precio_base']}")
                entrada = input("\n> Elige un combo: ").strip()
                if cancelacion_rapida(entrada):
                    return
                try:
                    id_combo = int(entrada)
                    # Se busca el combo seleccionado
                    combo_sel = next((c for c in combos if c["id"] == id_combo), None)
                    if combo_sel:
                        pedido["productos"] = combo_sel["productos"]
                        pedido["total"] = combo_sel["precio_base"]
                        pedido["combo"] = combo_sel["nombre"]
                        break
                    else:
                        print("\n >> Combo no encontrado.")
                        input("\n Presiona Enter para intentar de nuevo...")
                except:
                    mensaje_error()

        # Apartado para armar el pedido manualmente
        elif opcion == "1":
            # Se cargan todos los productos disponibles de los archivos JSON
            productos = (
                cargar_hamburguesas() + cargar_acompanamientos() + cargar_bebidas()
            )
            categorias = ["hamburguesas", "acompañamientos", "bebidas"]
            # Se recorre cada categoría para seleccionar un producto de cada una
            for cat in categorias:
                while True:
                    limpiar_consola()
                    encabezado_pedido()
                    print(f" <<--- Selecciona una {cat} --->>")
                    opciones = [p for p in productos if p["categoria"] == cat]
                    for prod in opciones:
                        print(f"{prod['id']}. {prod['nombre']} - ${prod['precio']}")
                    entrada = input("\n > Elige una opción: ").strip()
                    if cancelacion_rapida(entrada):
                        return
                    try:
                        id_sel = int(entrada)
                        # Se busca el producto seleccionado
                        prod_sel = next(
                            (p for p in opciones if p["id"] == id_sel), None
                        )
                        if prod_sel:
                            pedido["productos"].append(prod_sel)
                            pedido["total"] += prod_sel["precio"]
                            break
                        else:
                            mensaje_error()
                    except:
                        mensaje_error()

        # Sección que pregunta si se desea agregar aderezos
        while True:
            limpiar_consola()
            encabezado_pedido()
            print(" <<--- ¿Quieres agregar aderezos? --->>")
            print("1. Sí")
            print("2. No")
            entrada = input("\n > Elige una opción: ").strip()
            if cancelacion_rapida(entrada):
                return

            if entrada == "1":
                # Se solicita la cantidad de aderezos a agregar
                while True:
                    limpiar_consola()
                    encabezado_pedido()
                    print("<<--- Cantidad de Aderezos --->>")
                    cantidad = input(" > Ingresa un número: ").strip()
                    if cancelacion_rapida(cantidad):
                        return
                    try:
                        cantidad = int(cantidad)
                        if cantidad > 0:
                            pedido["cantidad_aderezos"] = cantidad
                        else:
                            pedido["cantidad_aderezos"] = 0
                        break
                    except:
                        mensaje_error()
                break

            elif entrada == "2":
                pedido["cantidad_aderezos"] = 0
                break
            else:
                mensaje_error()

        # Aplica recargo por exceso de aderezos
        exceso_aderezos = pedido["cantidad_aderezos"] - LIMITE_ADEREZOS_SIN_RECARGO
        if exceso_aderezos > 0:
            recargo_total = 0
            # Se calcula un recargo creciente según cantidad de aderezos extras
            for i in range(exceso_aderezos):
                recargo_total += RECARGO_ADEREZOS * (1.2**i)
            recargo_total = int(recargo_total)
            pedido["recargo_aderezos"] = recargo_total
            pedido["total"] += recargo_total
        else:
            pedido["recargo_aderezos"] = 0

        # Sección que pregunta si se desea personalizar el pedido
        if not personalizacion_pedido(pedido):
            return

        # Sección que solicita el nombre del cliente
        while True:
            limpiar_consola()
            encabezado_pedido()
            print("<<---- Datos del Cliente ---->>")
            cliente = input("¿A nombre de quién es el pedido?: ").strip()
            if cancelacion_rapida(cliente):
                return
            if cliente:
                pedido["cliente"] = cliente
                break
            print("\n >> El nombre no puede estar vacío.")
            input("\n Presiona Enter para intentar de nuevo...")

        # Sección que muestra un resumen del pedido y solicita confirmación
        if resumen_pedido(pedido):
            pedidos.append(pedido)
            guardar_pedidos(pedidos)
            print("\n----------------------------------\n")
            print(f"<<==== Pedido creado con éxito ====>>")
            print(f"> Número de ticket: {pedido['numero_ticket']}")
            input("\n Presiona Enter para continuar...")
        else:
            input("\n Presiona Enter para continuar...")

        # Sección que pregunta si se desea crear otro pedido
        while True:
            limpiar_consola()
            encabezado_pedido()
            print(" >> ¿Deseas crear otro pedido? <<")
            print("1. Sí")
            print("2. No, volver al menú de pedidos")
            opcion = input("\n > Elige una opción: ").strip()

            if opcion == "1":
                break
            elif opcion == "2":
                print("\n << Volviendo al menú de pedidos...")
                input("\n Presiona Enter para continuar...")
                return
            else:
                mensaje_error()

# Función para buscar un pedido por su número de ticket
def ver_pedido_por_ticket(pedidos):
    # Verifica si hay pedidos cargados
    if not pedidos:
        print("\n >> No hay pedidos cargados.")
        input("\n Presiona Enter para continuar...")
        return

    # Se cargan todos los productos para poder identificar los productos por nombre
    productos_base = cargar_hamburguesas() + cargar_acompanamientos() + cargar_bebidas()

    while True:
        limpiar_consola()
        print("\n[======== Buscar Pedido por Número de Ticket ========]")
        print(" <-- Coloca 'x' para salir -->\n")
        entrada = input("> Ingresa el número de ticket: ").strip()
        if cancelacion_rapida(entrada):
            return

        # Validación de entrada
        if not entrada.isdigit():
            mensaje_error()
            continue

        ticket_buscar = int(entrada)

        # Busca el pedido en la lista usando el número de ticket
        pedido = next(
            (p for p in pedidos if p.get("numero_ticket") == ticket_buscar), None
        )

        # Si no se encuentra el ticket
        if not pedido:
            print("\n >> Pedido no encontrado con ese número de ticket.")
            input("\n Presiona Enter para intentar con otro número...")
            continue

        # Si se encuentra el pedido, se muestra sus detalles
        while True:
            limpiar_consola()
            print("\n===== Buscar Pedido por Número de Ticket =====")
            print("\n<<<==== Detalles del Pedido ====>>>\n")
            print(f"Número de Ticket: {pedido.get('numero_ticket')}")
            print(f"Fecha y Hora: {pedido.get('fecha_hora')}")
            print(f"Cliente: {pedido['cliente']}")

            # Si el pedido fue hecho con un combo, se muestra su nombre
            if pedido.get("combo"):
                print(f"Combo: {pedido['combo']}")

            # Muestra los productos incluidos en el pedido
            print("Productos:")
            for prod in pedido["productos"]:
                # Si el producto es un diccionario, se muestra directamente
                if isinstance(prod, dict):
                    print(f"  - {prod['nombre']}: ${prod['precio']}")
                # Si es un string, se busca en la lista de productos
                elif isinstance(prod, str):
                    prod_info = next(
                        (p for p in productos_base if p["nombre"] == prod), None
                    )
                    if prod_info:
                        print(f"  - {prod}: ${prod_info['precio']}")
                    else:
                        print(f"  - {prod}: (precio no encontrado)")
                else:
                    print(f"  - {prod}: (formato no reconocido)")

            # Muestra la personalización del pedido si existe
            personalizaciones = []

            if pedido.get("tamaño_bebida"):
                recargo = pedido.get("recargo_tamaño_bebida", 0)
                texto = f"- Tamaño de bebida: {pedido['tamaño_bebida']}"
                if recargo > 0:
                    texto += f" (+${recargo})"
                personalizaciones.append(texto)

            if pedido.get("tamaño_papas"):
                recargo = pedido.get("recargo_tamaño_papas", 0)
                texto = f"- Tamaño de papas: {pedido['tamaño_papas']}"
                if recargo > 0:
                    texto += f" (+${recargo})"
                personalizaciones.append(texto)

            if pedido.get("tamaño_hamburguesa"):
                recargo = pedido.get("recargo_tamaño_hamburguesa", 0)
                texto = f"- Tamaño de hamburguesa: {pedido['tamaño_hamburguesa']}"
                if recargo > 0:
                    texto += f" (+${recargo})"
                personalizaciones.append(texto)

            # Si hay personalizaciones, se muestran en bloque
            if personalizaciones:
                print("Personalización:")
                for item in personalizaciones:
                    print(item)

            # Mostrar cantidad de aderezos y recargo si hay exceso
            if pedido.get("cantidad_aderezos", 0) > 0:
                print(f"Cantidad de aderezos: {pedido['cantidad_aderezos']}")
                if pedido.get("recargo_aderezos", 0) > 0:
                    print(
                        f"Recargo por exceso de aderezos: ${pedido['recargo_aderezos']}"
                    )

            # Mostrar el total final del pedido
            print(f"\nTotal: ${pedido['total']}")

            # Preguntar si se desea ver otro pedido
            print("\n----------------------------------")
            print(" >> ¿Deseas ver otro pedido? <<")
            print("1. Sí")
            print("2. No, volver al menú de pedidos")
            opcion = input("\n > Elige una opción: ").strip()

            if opcion == "1":
                break  # Vuelve al bucle principal para ingresar otro ticket
            elif opcion == "2":
                print("\n << Volviendo al menú de pedidos...")
                input("\n Presiona Enter para continuar...")
                return
            else:
                mensaje_error()

# Función que permite eliminar un pedido existente por su número de ticket
def eliminar_pedido(pedidos):
    # Verifica si hay pedidos cargados
    if not pedidos:
        print("\n >> No hay pedidos cargados.")
        input("\n Presiona Enter para continuar...")
        return

    while True:
        limpiar_consola()
        print("\n===== Eliminar Pedido por Número de Ticket =====")
        print("<-- Coloca 'x' para salir -->\n")

        # Se solicita el número de ticket a eliminar
        entrada = input("Ingresa el número de ticket: ").strip()
        if cancelacion_rapida(entrada):
            return  # Permite salir del proceso en cualquier momento

        # Validación de entrada
        if not entrada.isdigit():
            mensaje_error()
            continue

        ticket_eliminar = int(entrada)

        # Se busca el pedido con ese número de ticket
        pedido = next(
            (p for p in pedidos if p.get("numero_ticket") == ticket_eliminar), None
        )

        # Si no se encuentra, se informa y se vuelve a pedir
        if not pedido:
            print(f"\n >> No se encontró un pedido con el ticket {ticket_eliminar}.")
            input("\n Presiona Enter para intentar de nuevo...")
            continue

        # Si se encuentra el pedido, se elimina de la lista
        pedidos.remove(pedido)
        guardar_pedidos(pedidos)
        print(f"\n >> Pedido con ticket {ticket_eliminar} eliminado con éxito.")

        # Preguntar si se desea eliminar otro pedido
        while True:
            limpiar_consola()
            print("\n===== Eliminar Pedido por Número de Ticket =====")
            print(f"\n >> Pedido con ticket {ticket_eliminar} eliminado con éxito! <<")
            print("\n --------------------------------------")
            print(" >> ¿Deseas eliminar otro pedido? <<")
            print("1. Sí")
            print("2. No, volver al menú de pedidos")
            opcion = input("\n > Elige una opción: ").strip()

            if opcion == "1":
                break
            elif opcion == "2":
                print("\n << Volviendo al menú de pedidos...")
                input("\n Presiona Enter para continuar...")
                return
            else:
                mensaje_error()

# Función que muestra el menú de gestión de pedidos
def menu_pedidos():
    # Se cargan los pedidos y combos existentes desde los archivos JSON
    pedidos = cargar_pedidos()
    combos = cargar_combos()

    while True:
        limpiar_consola()
        print("\n[======== Menú de Gestión de Pedidos ========]\n")
        print("1. Crear pedido")
        print("2. Buscar pedido (Nrm Ticket)")
        print("3. Eliminar pedido (Nrm Ticket)")
        print("4. Volver al Menú Principal")

        opcion = input("\n> Ingrese una opción: ").strip()

        if not opcion.isdigit():
            mensaje_error()
            continue

        opcion = int(opcion)

        if opcion == 1:
            crear_pedido(pedidos, combos)
        elif opcion == 2:
            ver_pedido_por_ticket(pedidos)
        elif opcion == 3:
            eliminar_pedido(pedidos)
        elif opcion == 4:
            print("\n << Saliendo del menú de Pedidos.")
            input("\n Presiona Enter para continuar...")
            break
        else:
            mensaje_error() 

# Iniciar el programa sin pasar por el main.py
if __name__ == "__main__":
    menu_pedidos()
