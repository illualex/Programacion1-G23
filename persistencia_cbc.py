import json
import os

RUTA_PRODUCTOS = 'datos/productos.json'
RUTA_PEDIDOS = 'datos/pedidos.json'
RUTA_COMBOS = 'datos/combos.json'

def cargar_archivo(ruta):
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def guardar_archivo(ruta, datos):
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def cargar_productos():
    return cargar_archivo(RUTA_PRODUCTOS)

def guardar_productos(productos):
    guardar_archivo(RUTA_PRODUCTOS, productos)

def cargar_pedidos():
    return cargar_archivo(RUTA_PEDIDOS)

def guardar_pedidos(pedidos):
    guardar_archivo(RUTA_PEDIDOS, pedidos)

def cargar_combos():
    return cargar_archivo(RUTA_COMBOS)