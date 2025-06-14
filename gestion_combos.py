from persistencia_cbc import cargar_combos

def mostrar_combos_disponibles():
    combos = cargar_combos()
    if not combos:
        print("\nNo hay combos cargados actualmente.\n")
        return

    print("\n--- Combos Disponibles ---")
    for combo in combos:
        print(f"\nID: {combo.get('id', 'N/A')}")
        print(f"Nombre: {combo.get('nombre')}")
        print("Productos incluidos:")
        for item in combo.get("productos", []):
            print(f"  - {item}")
        print(f"Precio: ${combo.get('precio')}")
    print()

def obtener_combos_disponibles():
    return cargar_combos()
