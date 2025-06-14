import os

def validar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor ingresá un número válido.")

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

