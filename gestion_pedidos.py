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
# === Recargos extra por aderezos ===
LIMITE_ADEREZOS_SIN_RECARGO = 5
RECARGO_ADEREZOS = 100

# === Recargos extra por personalización ===
RECARGO_BEBIDA_MEDIANA = 300
RECARGO_BEBIDA_GRANDE = 500

RECARGO_ACOMPANAMIENTO_MEDIANAS = 400
RECARGO_ACOMPANAMIENTO_GRANDES = 600

RECARGO_HAMBURGUESA_MEDIANA = 600
RECARGO_HAMBURGUESA_GRANDE = 1000


# ====== FUNCIONES AUXILIARES ======
# === Generar número de ticket random de 5 dígitos ===
def generar_numero_ticket():
    return random.randint(10000, 99999)

# === Encabezado de armado del pedido ===
def encabezado_pedido():
    print("\n======== Armado de Pedido ========")
    print("- Salida rápida coloca 'x' -\n")

# === Personalización del pedido ===
def personalizacion_pedido(pedido):
    while True:
        limpiar_consola()
        encabezado_pedido()
        print(" <--- ¿Quieres agrandar el pedido? --->")
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
                print(" <--- Elige el tamaño de la bebida --->")
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
                print("<--- Elige el tamaño del acompañamiento --->")
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
                print(" <--- Elige el tamaño de la hamburguesa --->\n")
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


# === Resumen del pedido ===
def resumen_pedido(pedido):
    while True:
        limpiar_consola()
        encabezado_pedido()
        print("<----- Resumen del Pedido ----->")
        print(f"Cliente: {pedido['cliente']}")

        if pedido.get("combo"):
            print(f"\nCombo: {pedido['combo']}")

        print("\nProductos:")
        for prod in pedido["productos"]:
            if isinstance(prod, dict):
                print(f"- {prod['nombre']}: ${prod['precio']}")
            else:
                print(f"- {prod}")  # Fallback si no tiene precio

        # Aderezos (si hay)
        if pedido["cantidad_aderezos"] > 0:
            print(f"\nAderezos: {pedido['cantidad_aderezos']}")
            if pedido.get("recargo_aderezos", 0) > 0:
                print(f"Recargo por exceso de aderezos: ${pedido['recargo_aderezos']}")

        # Personalización (si hay)
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
        print("\n >>> ¿Deseas confirmar este pedido? <<<")
        print("1. Confirmar y guardar")
        print("2. Cancelar")
        eleccion = input("\n > Elige una opción: ").strip()

        if eleccion == "1":
            return True
        elif eleccion == "2":
            print("\n >> Pedido cancelado.")
            return False
        else:
            mensaje_error()


# ====== FUNCIONES PRINCIPALES ======
# === Crear Pedido ===
def crear_pedido(pedidos, combos):
    while True:
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

        # Selección de productos o combo
        while True:
            limpiar_consola()
            encabezado_pedido()
            print(" <--- ¿Qué quieres ordenar? --->")
            print("1. Armar tu pedido")
            print("2. Elegir un combo")
            opcion = input("\n > Elige una opción: ").strip()
            if cancelacion_rapida(opcion):
                return
            if opcion in ["1", "2"]:
                break
            mensaje_error()

        if opcion == "2":
            while True:
                limpiar_consola()
                encabezado_pedido()
                print(" <--- Combos disponibles --->")
                for combo in combos:
                    print(f"{combo['id']}. {combo['nombre']}: ${combo['precio_base']}")
                entrada = input("\n> Elige un combo: ").strip()
                if cancelacion_rapida(entrada):
                    return
                try:
                    id_combo = int(entrada)
                    combo_sel = next((c for c in combos if c["id"] == id_combo), None)
                    if combo_sel:
                        pedido["productos"] = combo_sel["productos"]
                        pedido["total"] = combo_sel["precio_base"]
                        pedido["combo"] = combo_sel["nombre"]
                        break
                    else:
                        print(">> Combo no encontrado.")
                except:
                    mensaje_error()

        elif opcion == "1":
            productos = (
                cargar_hamburguesas() + cargar_acompanamientos() + cargar_bebidas()
            )
            categorias = ["hamburguesas", "acompañamientos", "bebidas"]
            for cat in categorias:
                while True:
                    limpiar_consola()
                    encabezado_pedido()
                    print(f" <--- Selecciona una {cat} --->")
                    opciones = [p for p in productos if p["categoria"] == cat]
                    for prod in opciones:
                        print(f"{prod['id']}. {prod['nombre']} - ${prod['precio']}")
                    entrada = input("\n > Elige una opción: ").strip()
                    if cancelacion_rapida(entrada):
                        return
                    try:
                        id_sel = int(entrada)
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

        # Aderezos
        while True:
            limpiar_consola()
            encabezado_pedido()
            print(" <--- ¿Quieres agregar aderezos? --->")
            print("1. Sí")
            print("2. No")
            entrada = input("\n > Elige una opción: ").strip()
            if cancelacion_rapida(entrada):
                return

            if entrada == "1":
                while True:
                    limpiar_consola()
                    encabezado_pedido()
                    print("<--- Cantidad de Aderezos --->")
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

        # Aplicar recargo si hay exceso de aderezos
        exceso_aderezos = pedido["cantidad_aderezos"] - LIMITE_ADEREZOS_SIN_RECARGO

        if exceso_aderezos > 0:
            recargo_total = 0
            for i in range(exceso_aderezos):
                recargo_total += RECARGO_ADEREZOS * (1.2**i)
            recargo_total = int(recargo_total)  # Redondeamos a entero
            pedido["recargo_aderezos"] = recargo_total
            pedido["total"] += recargo_total
        else:
            pedido["recargo_aderezos"] = 0

        # Personalización
        if not personalizacion_pedido(pedido):
            return

        # Cliente
        while True:
            limpiar_consola()
            encabezado_pedido()
            print("<----- Datos del Cliente ----->")
            cliente = input("¿A nombre de quién es el pedido?: ").strip()
            if cancelacion_rapida(cliente):
                return
            if cliente:
                pedido["cliente"] = cliente
                break
            print("\n >> El nombre no puede estar vacío.")
            input("\n Presiona Enter para intentar de nuevo...")

        # Confirmar y guardar
        if resumen_pedido(pedido):
            pedidos.append(pedido)
            guardar_pedidos(pedidos)
            print("\n----------------------------------\n")
            print(f"<<=== Pedido creado con éxito ===>>")
            print(f"> Número de ticket: {pedido['numero_ticket']}")
            input("\n Presiona Enter para continuar...")
        else:
            input("\n Presiona Enter para continuar...")

        # Crear otro pedido o salir
        while True:
            limpiar_consola()
            encabezado_pedido()
            print(" <<< ¿Deseas crear otro pedido? >>>")
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


# === Ver Pedido por Ticket ===
def ver_pedido_por_ticket(pedidos):
    if not pedidos:
        print("\n >> No hay pedidos cargados.")
        input("\n Presiona Enter para continuar...")
        return

    productos_base = cargar_hamburguesas() + cargar_acompanamientos() + cargar_bebidas()

    while True:
        limpiar_consola()
        print("\n===== Buscar Pedido por Número de Ticket =====")
        print(" <-- Coloca 'x' para salir -->\n")
        entrada = input("> Ingresa el número de ticket: ").strip()
        if cancelacion_rapida(entrada):
            return

        if not entrada.isdigit():
            mensaje_error()
            continue

        ticket_buscar = int(entrada)
        pedido = next(
            (p for p in pedidos if p.get("numero_ticket") == ticket_buscar), None
        )

        # Si el ticket no fue encontrado
        if not pedido:
            print("\n >> Pedido no encontrado con ese número de ticket.")
            input("\n Presiona Enter para intentar con otro número...")
            continue

        # Si el ticket fue encontrado
        while True:
            limpiar_consola()
            print("\n===== Buscar Pedido por Número de Ticket =====")
            print("\n<<<==== Detalles del Pedido ====>>>\n")
            print(f"Número de Ticket: {pedido.get('numero_ticket')}")
            print(f"Fecha y Hora: {pedido.get('fecha_hora')}")
            print(f"Cliente: {pedido['cliente']}")

            if pedido.get("combo"):
                print(f"Combo: {pedido['combo']}")

            print("Productos:")
            for prod in pedido["productos"]:
                if isinstance(prod, dict):
                    print(f"  - {prod['nombre']}: ${prod['precio']}")
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
                print("Personalización:")
                for item in personalizaciones:
                    print(item)

            if pedido.get("cantidad_aderezos", 0) > 0:
                print(f"Cantidad de aderezos: {pedido['cantidad_aderezos']}")
                if pedido.get("recargo_aderezos", 0) > 0:
                    print(
                        f"Recargo por exceso de aderezos: ${pedido['recargo_aderezos']}"
                    )

            print(f"\nTotal: ${pedido['total']}")

            # Confirmar si desea ver otro pedido
            print("\n -->>> ¿Deseas ver otro pedido? <<<--")
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


# === Eliminar Pedido por Ticket ===
def eliminar_pedido(pedidos):
    if not pedidos:
        print("\n >> No hay pedidos cargados.")
        input("\n Presiona Enter para continuar...")
        return

    while True:
        limpiar_consola()
        print("\n===== Eliminar Pedido por Número de Ticket =====")
        print("<-- Coloca 'x' para salir -->\n")

        entrada = input("Ingresa el número de ticket: ").strip()
        if cancelacion_rapida(entrada):
            return

        if not entrada.isdigit():
            mensaje_error()
            continue

        ticket_eliminar = int(entrada)
        pedido = next(
            (p for p in pedidos if p.get("numero_ticket") == ticket_eliminar), None
        )

        if not pedido:
            print(f"\n >> No se encontró un pedido con el ticket {ticket_eliminar}.")
            input("\n Presiona Enter para intentar de nuevo...")
            continue

        pedidos.remove(pedido)
        guardar_pedidos(pedidos)
        print(f"\n >> Pedido con ticket {ticket_eliminar} eliminado con éxito.")

        # Preguntar si desea eliminar otro
        while True:
            limpiar_consola()
            print("\n===== Eliminar Pedido por Número de Ticket =====")
            print(f"\n >> Pedido con ticket {ticket_eliminar} eliminado con éxito.")
            print("\n -->>> ¿Deseas eliminar otro pedido? <<<--")
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


# ===== Menu de pedidos =====
def menu_pedidos():
    pedidos = cargar_pedidos()
    combos = cargar_combos()

    while True:
        limpiar_consola()
        print("\n===== Menu de Gestión de Pedidos =====")
        print("1. Crear pedido")
        print("2. Buscar pedido [Nrm Ticket]")
        print("3. Eliminar pedido [Nrm Ticket]")
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
            print("\n << Saliendo del menú de pedidos.")
            input("\n Presiona Enter para continuar...")
            break
        else:
            mensaje_error()


if __name__ == "__main__":
    menu_pedidos()
