import json
from persistencia_cbc import cargar_pedidos, guardar_pedidos
from gestion_productos import cargar_productos
from gestion_combos import cargar_combos

def personalizar_pedido(pedido):
    print("¿Querés agrandar el pedido? (s/n)")
    respuesta = input().strip().lower()
    if respuesta != 's':
        print("No se hacen cambios al pedido.")
        return pedido

    # Tamaño de bebida
    print("Elige tamaño de bebida (chico, mediano, grande):")
    tam_bebida = input().strip().lower()
    if tam_bebida == 'mediano':
        pedido['total'] += 300
    elif tam_bebida == 'grande':
        pedido['total'] += 500
    pedido['tamaño_bebida'] = tam_bebida

    # Tamaño de papas
    print("Elige tamaño de papas (chico, mediano, grande):")
    tam_papas = input().strip().lower()
    if tam_papas == 'mediano':
        pedido['total'] += 400
    elif tam_papas == 'grande':
        pedido['total'] += 600
    pedido['tamaño_papas'] = tam_papas

    # Tamaño de hamburguesa
    print("Elige tamaño de hamburguesa (simple, doble, triple):")
    tam_hambu = input().strip().lower()
    if tam_hambu == 'doble':
        pedido['total'] += 600
    elif tam_hambu == 'triple':
        pedido['total'] += 1000
    pedido['tamaño_hamburguesa'] = tam_hambu

    # Aderezos
    print("Querés agregar aderezos? (s/n)")
    respuesta = input().strip().lower()
    if respuesta == 's':
        print("Escribí los aderezos separados por coma (ej: mayonesa, mostaza, ketchup, sal):")
        aderezos = input().strip().lower().split(',')
        pedido['aderezos'] = [a.strip() for a in aderezos if a.strip()]
    else:
        pedido['aderezos'] = []

    print("Pedido personalizado con éxito.")
    return pedido

def crear_pedido(productos, combos, pedidos):
    print("¿Querés pedir un combo (c) o productos sueltos (p)?")
    opcion = input().strip().lower()

    pedido = {
        "id": len(pedidos) + 1,
        "productos": [],
        "total": 0,
        "tamaño_bebida": None,
        "tamaño_papas": None,
        "tamaño_hamburguesa": None,
        "aderezos": []
    }

    if opcion == 'c':
        print("Combos disponibles:")
        for combo in combos:
            print(f"{combo['id']}. {combo['nombre']} - Precio base: ${combo['precio_base']}")

        id_combo = int(input("Elegí el ID del combo: "))
        combo_seleccionado = next((c for c in combos if c['id'] == id_combo), None)
        if combo_seleccionado:
            pedido['productos'] = [p['nombre'] for p in combo_seleccionado['productos']]
            pedido['total'] = combo_seleccionado['precio_base']
        else:
            print("Combo no encontrado.")
            return

    elif opcion == 'p':
        print("Productos disponibles:")
        for producto in productos:
            print(f"{producto['id']}. {producto['nombre']} - ${producto['precio']}")
        print("Ingresá los IDs de los productos separados por coma:")
        ids = input().split(',')
        total = 0
        seleccionados = []
        for i in ids:
            try:
                idp = int(i.strip())
                prod = next((p for p in productos if p['id'] == idp), None)
                if prod:
                    seleccionados.append(prod['nombre'])
                    total += prod['precio']
            except:
                continue
        pedido['productos'] = seleccionados
        pedido['total'] = total
    else:
        print("Opción inválida.")
        return

    pedido = personalizar_pedido(pedido)
    pedidos.append(pedido)
    guardar_pedidos(pedidos)
    print("Pedido creado y guardado con éxito.")

def listar_pedidos(pedidos):
    if not pedidos:
        print("No hay pedidos cargados.")
        return
    for p in pedidos:
        print(f"ID: {p['id']} - Productos: {', '.join(p['productos'])} - Total: ${p['total']}")
        if p.get('tamaño_bebida'):
            print(f"  Bebida: {p['tamaño_bebida']}")
        if p.get('tamaño_papas'):
            print(f"  Papas: {p['tamaño_papas']}")
        if p.get('tamaño_hamburguesa'):
            print(f"  Hamburguesa: {p['tamaño_hamburguesa']}")
        if p.get('aderezos'):
            print(f"  Aderezos: {', '.join(p['aderezos'])}")

def eliminar_pedido(pedidos):
    listar_pedidos(pedidos)
    id_eliminar = int(input("Ingresá el ID del pedido a eliminar: "))
    pedido = next((p for p in pedidos if p['id'] == id_eliminar), None)
    if pedido:
        pedidos.remove(pedido)
        guardar_pedidos(pedidos)
        print("Pedido eliminado.")
    else:
        print("Pedido no encontrado.")

def menu_pedidos():
    pedidos = cargar_pedidos()
    productos = cargar_productos()
    combos = cargar_combos()

    while True:
        print("\n--- Menú de Pedidos ---")
        print("1. Crear pedido")
        print("2. Listar pedidos")
        print("3. Eliminar pedido")
        print("4. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == '1':
            crear_pedido(productos, combos, pedidos)
        elif opcion == '2':
            listar_pedidos(pedidos)
        elif opcion == '3':
            eliminar_pedido(pedidos)
        elif opcion == '4':
            print("Saliendo del menú de pedidos.")
            break
        else:
            print("Opción inválida, intentá de nuevo.")

if __name__ == "__main__":
    menu_pedidos()
