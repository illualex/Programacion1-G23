import json
from persistencia_cbc import cargar_pedidos
from utils_cbc import limpiar_consola, mensaje_error, cancelacion_rapida
from datetime import datetime, timedelta


# ===== FUNCIONES AUXILIARES =====
# Función para mostrar el encabezado del reporte de ventas
def encabezado_ventas():
    print("\n[======== Ventas de la Semana ========]")
    print(" - Salida rápida coloca 'x' -\n")


# Función para filtrar pedidos de la última semana
def filtrar_pedidos_ultima_semana(pedidos):
    hoy = datetime.now()
    hace_7_dias = hoy - timedelta(days=7)
    pedidos_semana = []
    for p in pedidos:
        try:
            # Convierte la fecha del pedido desde string a objeto datetime
            fecha = datetime.strptime(p["fecha_hora"], "%Y-%m-%d %H:%M:%S")
            if fecha >= hace_7_dias:
                pedidos_semana.append(p)
        except:
            continue
    return pedidos_semana


# ===== FUNCIONES PRINCIPALES =====
# Función que genera el reporte de ventas de la última semana
def reporte_ventas_semana():
    pedidos = cargar_pedidos()

    # Verifica si hay pedidos cargados
    if not pedidos:
        limpiar_consola()
        encabezado_ventas()
        print("\n >> No hay pedidos registrados.")
        input("\n Presiona Enter para volver...")
        return

    # Pide al usuario qué vista desea ver (simple o detallada)
    while True:
        limpiar_consola()
        encabezado_ventas()
        print("1. Vista simple")
        print("2. Vista detallada")
        vista = input("\n > Elige una vista: ").strip()

        if cancelacion_rapida(vista):
            return
        if vista not in ["1", "2"]:
            mensaje_error()
        else:
            break

    # Filtra pedidos de la última semana
    pedidos_semana = filtrar_pedidos_ultima_semana(pedidos)

    if not pedidos_semana:
        limpiar_consola()
        encabezado_ventas()
        print("\n >> No hay pedidos registrados en los últimos 7 días.")
        input("\n Presiona Enter para volver...")
        return

    # Calcula totales
    total_ventas = len(pedidos_semana)
    monto_total = sum(p["total"] for p in pedidos_semana)
    limpiar_consola()
    encabezado_ventas()

    # Vista detallada: muestra cada ticket con cliente y total
    if vista == "2":
        print("<<--- Vista Detallada de ventas --->>\n")
        for p in pedidos_semana:
            print(
                f"Ticket: {p['numero_ticket']} - Cliente: {p['cliente']} - Total: ${p['total']} - Fecha: {p['fecha_hora']}"
            )
    # Vista simple: solo resumen
    else:
        print("<<--- Vista Simple de ventas --->>")

    print(f"\n- Total de pedidos: {total_ventas}")
    print(f"- Monto total recaudado: ${monto_total}")
    input("\n Presiona Enter para volver al menu...")


# Función que genera el reporte de productos más vendidos en la última semana
def reporte_productos_mas_vendidos():
    limpiar_consola()
    print("[======== Productos Más Vendidos (Últimos 7 Días) ========]")
    pedidos = cargar_pedidos()

    if not pedidos:
        print("\n >> No hay pedidos registrados.")
        input("\n Presiona Enter para volver...")
        return

    pedidos_semana = filtrar_pedidos_ultima_semana(pedidos)

    if not pedidos_semana:
        print("\n >> No hay pedidos en la última semana.")
        input("\n Presiona Enter para volver...")
        return

    # Diccionario para contar productos vendidos
    categorias = {
        "hamburguesas": {},
        "acompañamientos": {},
        "bebidas": {},
        "combos": {},
    }

    # Diccionario para contar tamaños pedidos por tipo
    personalizacion = {
        "hamburguesas": {"chica": 0, "mediano": 0, "grande": 0},
        "acompañamientos": {"chica": 0, "mediano": 0, "grande": 0},
        "bebidas": {"chica": 0, "mediano": 0, "grande": 0},
    }

    # Suma total de aderezos pedidos
    total_aderezos = 0

    # Recorre cada pedido de la semana
    for pedido in pedidos_semana:
        # Suma combos vendidos
        if pedido.get("combo"):
            combo_nombre = pedido["combo"]
            categorias["combos"][combo_nombre] = (
                categorias["combos"].get(combo_nombre, 0) + 1
            )

        # Suma productos individuales vendidos
        for producto in pedido["productos"]:
            if isinstance(producto, dict):
                cat = producto.get("categoria", "otros")
                nombre = producto["nombre"]
                categorias.setdefault(cat, {})
                categorias[cat][nombre] = categorias[cat].get(nombre, 0) + 1

        # Suma personalizaciones por tamaño
        tipo_a_categoria = {
            "hamburguesa": "hamburguesas",
            "bebida": "bebidas",
            "papas": "acompañamientos",
        }
        for tipo_singular, tipo_plural in tipo_a_categoria.items():
            key = f"tamaño_{tipo_singular}"
            tam = pedido.get(key)
            if tam in ["chica", "mediano", "grande"]:
                personalizacion[tipo_plural][tam] += 1

        # Suma cantidad de aderezos
        total_aderezos += pedido.get("cantidad_aderezos", 0)

    # Muestra productos más vendidos por categoría
    for cat, productos in categorias.items():
        print(f"\n>> {cat.capitalize()} <<")
        if not productos:
            print("No hay ventas registradas.")
            continue
        for nombre, cantidad in sorted(
            productos.items(), key=lambda x: x[1], reverse=True
        ):
            print(f"- {nombre}: {cantidad} ventas")

    # Muestra total de aderezos
    print("\n>> Aderezos <<")
    print(f"- Cantidad: {total_aderezos} ventas")

    # Muestra personalizaciones pedidas
    print("\n<<--- Personalizaciones Pedidas --->>")
    for cat, tamaños in personalizacion.items():
        print(f"\n> {cat.capitalize()} <")
        for tam, cantidad in tamaños.items():
            print(f"- {tam}: {cantidad} veces")

    input("\n Presiona Enter para volver al menú...")


# Función que calcula el promedio de gasto por pedido en la última semana
def reporte_promedio_gasto():
    limpiar_consola()
    print("\n[======== Promedio de Gasto por Pedido ========]\n")
    pedidos = cargar_pedidos()

    if not pedidos:
        print("\n >> No hay pedidos registrados.")
        input("\n Presiona Enter para volver...")
        return

    pedidos_semana = filtrar_pedidos_ultima_semana(pedidos)

    if not pedidos_semana:
        print("\n >> No hay pedidos en la última semana.")
        input("\n Presiona Enter para volver...")
        return

    # Cálculo del promedio
    total_gasto = sum(p["total"] for p in pedidos_semana)
    promedio = total_gasto // len(pedidos_semana)
    print("<<--- Promedio de esta semana --->>")
    print(f"- Cantidad de pedidos: {len(pedidos_semana)}")
    print(f"- Gasto total acumulado: ${total_gasto}")
    print(f"- Promedio de gasto por pedido: ${promedio}")
    input("\n Presiona Enter para volver al menú...")


# Función que muestra el menú de reportes
def menu_reportes():
    while True:
        limpiar_consola()
        print("\n[======== Menu de Reportes ========]\n")
        print("1. Listar ventas de la semana")
        print("2. Productos más vendidos")
        print("3. Promedio de gasto por pedido")
        print("4. Volver al menú principal")

        opcion = input("\n > Ingrese una opción: ").strip()
        if opcion == "1":
            reporte_ventas_semana()
        elif opcion == "2":
            reporte_productos_mas_vendidos()
        elif opcion == "3":
            reporte_promedio_gasto()
        elif opcion == "4":
            print("\n << Saliendo del menú de Reportes.")
            input("\n Presiona Enter para continuar...")
            break
        else:
            mensaje_error()


# Iniciar el programa sin pasar por el main.py
if __name__ == "__main__":
    menu_reportes()
