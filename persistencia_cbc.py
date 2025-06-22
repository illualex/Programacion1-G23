import json
import os

# === Rutas a los archivos JSON ===
RUTA_HAMBURGUESAS = "datos/hamburguesas.json"
RUTA_BEBIDAS = "datos/bebidas.json"
RUTA_ACOMPANAMIENTOS = "datos/acompanamientos.json"
RUTA_PEDIDOS = "datos/pedidos.json"
RUTA_COMBOS = "datos/combos.json"


# === Funciones genéricas ===
def cargar_archivo(ruta):
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_archivo(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


# === Cargar productos por tipo ===
def cargar_hamburguesas():
    return cargar_archivo(RUTA_HAMBURGUESAS)


def cargar_bebidas():
    return cargar_archivo(RUTA_BEBIDAS)


def cargar_acompanamientos():
    return cargar_archivo(RUTA_ACOMPANAMIENTOS)


# === Guardar productos por tipo ===
def guardar_hamburguesas(datos):
    guardar_archivo(RUTA_HAMBURGUESAS, datos)


def guardar_bebidas(datos):
    guardar_archivo(RUTA_BEBIDAS, datos)


def guardar_acompanamientos(datos):
    guardar_archivo(RUTA_ACOMPANAMIENTOS, datos)


# === Unificar productos (para listados, reportes, etc.) ===
def cargar_todos_los_productos():
    return cargar_hamburguesas() + cargar_bebidas() + cargar_acompanamientos()


# === Pedidos ===
def cargar_pedidos():
    return cargar_archivo(RUTA_PEDIDOS)


def guardar_pedidos(pedidos):
    guardar_archivo(RUTA_PEDIDOS, pedidos)


# === Combos ===
def cargar_combos():
    return cargar_archivo(RUTA_COMBOS)


def guardar_combos(combos):
    guardar_archivo(RUTA_COMBOS, combos)
