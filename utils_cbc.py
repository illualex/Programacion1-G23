import os

# Función para limpiar la consola
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


# Funcion para mostrar un mensaje de error estándar
def mensaje_error():
    print("\n >> Opción inválida.")
    input("\n Presiona Enter para intentar de nuevo...")


# Funcion para cancelar una operación rápida
def cancelacion_rapida(entrada):
    if entrada.strip().lower() == "x":
        print("\n << Operación cancelada. Volviendo al menú...")
        input("\n Presiona Enter para continuar...")
        return True
    return False

# Función para exportar un ticket de pedido a un archivo de texto
def exportar_ticket_txt(pedido):
    carpeta = "tickets"
    # Crea la carpeta "tickets" si no existe
    os.makedirs(carpeta, exist_ok=True)

    # Define el nombre del archivo usando el número de ticket (ej: ticket_12345.txt)
    nombre_archivo = os.path.join(carpeta, f"ticket_{pedido['numero_ticket']}.txt")

    # Abre el archivo en modo escritura y con codificación UTF-8
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        # Encabezado del ticket
        archivo.write("===== Ticket de Pedido =====\n\n")
        archivo.write(f"Fecha y Hora: {pedido['fecha_hora']}\n")
        archivo.write(f"Número de Ticket: {pedido['numero_ticket']}\n")
        archivo.write(f"Cliente: {pedido['cliente']}\n\n")

        # Si el pedido se hizo con un combo, se muestra su nombre
        if pedido.get("combo"):
            archivo.write(f"Combo: {pedido['combo']}\n\n")

        # Lista de productos del pedido
        archivo.write("Productos:\n")
        for prod in pedido["productos"]:
            if isinstance(prod, dict):
                archivo.write(f" - {prod['nombre']}: ${prod['precio']}\n")
            else:
                archivo.write(f" - {prod}\n")

        # Información de aderezos
        if pedido["cantidad_aderezos"] > 0:
            archivo.write(f"\nAderezos: {pedido['cantidad_aderezos']}\n")
            if pedido.get("recargo_aderezos", 0) > 0:
                archivo.write(f"Recargo por exceso de aderezos: ${pedido['recargo_aderezos']}\n")

        # Personalización de tamaño de bebida (si existe)
        if pedido.get("tamaño_bebida"):
            recargo = pedido.get("recargo_tamaño_bebida", 0)
            archivo.write(f"Tamaño de bebida: {pedido['tamaño_bebida']}")
            if recargo > 0:
                archivo.write(f" (+${recargo})")
            archivo.write("\n")

        # Personalización de tamaño de papas (si existe)
        if pedido.get("tamaño_papas"):
            recargo = pedido.get("recargo_tamaño_papas", 0)
            archivo.write(f"Tamaño de papas: {pedido['tamaño_papas']}")
            if recargo > 0:
                archivo.write(f" (+${recargo})")
            archivo.write("\n")

        # Personalización de tamaño de hamburguesa (si existe)
        if pedido.get("tamaño_hamburguesa"):
            recargo = pedido.get("recargo_tamaño_hamburguesa", 0)
            archivo.write(f"Tamaño de hamburguesa: {pedido['tamaño_hamburguesa']}")
            if recargo > 0:
                archivo.write(f" (+${recargo})")
            archivo.write("\n")

        # Total del pedido y mensaje final
        archivo.write(f"\nTotal a pagar: ${pedido['total']}\n")
        archivo.write("\nGracias por tu compra!\n")
        archivo.write("--- Concordia Burger Club - 2025 ---")
