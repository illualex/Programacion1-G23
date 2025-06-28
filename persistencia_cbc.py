import json
import os

# Constantes para las rutas de los archivos JSON que almacenan los productos, pedidos y combos.
RUTA_HAMBURGUESAS = "datos/hamburguesas.json"
RUTA_BEBIDAS = "datos/bebidas.json"
RUTA_ACOMPANAMIENTOS = "datos/acompanamientos.json"
RUTA_PEDIDOS = "datos/pedidos.json"
RUTA_COMBOS = "datos/combos.json"


# ===== FUNCIÓN GENERAL =====
# Carga los datos desde un archivo JSON si existe. si no, retorna una lista vacía.
def cargar_archivo(ruta):
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# Guarda los datos en un archivo JSON, con formato legible (indentado).
def guardar_archivo(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


# ===== CARGA DE DATOS =====
# Carga la lista de hamburguesas desde su archivo JSON correspondiente.
def cargar_hamburguesas():
    return cargar_archivo(RUTA_HAMBURGUESAS)


# Carga la lista de bebidas desde su archivo JSON correspondiente.
def cargar_bebidas():
    return cargar_archivo(RUTA_BEBIDAS)


# Carga la lista de acompañamientos desde su archivo JSON correspondiente.
def cargar_acompanamientos():
    return cargar_archivo(RUTA_ACOMPANAMIENTOS)


# ===== GUARDADO DE DATOS =====
# Guarda la lista de hamburguesas en su archivo JSON correspondiente.
def guardar_hamburguesas(datos):
    guardar_archivo(RUTA_HAMBURGUESAS, datos)


# Guarda la lista de bebidas en su archivo JSON correspondiente.
def guardar_bebidas(datos):
    guardar_archivo(RUTA_BEBIDAS, datos)


# Guarda la lista de acompañamientos en su archivo JSON correspondiente.
def guardar_acompanamientos(datos):
    guardar_archivo(RUTA_ACOMPANAMIENTOS, datos)

# ===== PEDIDOS =====
# Carga todos los pedidos desde el archivo JSON correspondiente.
def cargar_pedidos():
    return cargar_archivo(RUTA_PEDIDOS)


# Guarda la lista de pedidos en el archivo JSON correspondiente.
def guardar_pedidos(pedidos):
    guardar_archivo(RUTA_PEDIDOS, pedidos)


# ===== COMBOS =====
# Carga la lista de combos desde el archivo JSON correspondiente.
def cargar_combos():
    return cargar_archivo(RUTA_COMBOS)


# Guarda la lista de combos en el archivo JSON correspondiente.
def guardar_combos(combos):
    guardar_archivo(RUTA_COMBOS, combos)
