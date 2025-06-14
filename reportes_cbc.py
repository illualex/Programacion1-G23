from persistencia_cbc import cargar_pedidos

def menu_reportes():
    pedidos = cargar_pedidos()
    if not pedidos:
        print("No hay pedidos registrados.")
        return

    total_ventas = sum(p['total'] for p in pedidos)
    print(f"Total recaudado: ${total_ventas}")

    productos_contados = {}
    for pedido in pedidos:
        for prod in pedido['productos']:
            productos_contados[prod] = productos_contados.get(prod, 0) + 1

    if productos_contados:
        mas_vendido = max(productos_contados, key=productos_contados.get)
        print(f"Producto más vendido: {mas_vendido} ({productos_contados[mas_vendido]} ventas)")
    else:
        print("No se encontraron productos en los pedidos.")

    print("Listado de pedidos:")
    for p in pedidos:
        print(f"ID: {p['id']} - ${p['total']} - {', '.join(p['productos'])}")
