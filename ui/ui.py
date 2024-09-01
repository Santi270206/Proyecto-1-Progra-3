import pandas as pd
from tabulate import tabulate

def obtener_entrada_usuario():
    nombre_departamento = input("Ingrese el nombre del departamento que desea consultar (En mayusculas): ").upper()
    
    while True:
        try:
            limite_registros = int(input("Ingrese el número de registros que desea obtener (entre 1 y 1000): "))
            if 1 <= limite_registros <= 1000:
                break
            else:
                print("El número de registros debe estar entre 1 y 1000. Intente de nuevo.")
        except ValueError:
            print("Debe ingresar un número entero válido. Intente de nuevo.")
    
    return nombre_departamento, limite_registros

def mostrar_datos(datos):
    if not datos:
        print("No se obtuvieron datos.")
        return
    
    # Muestra los datos en una tabla si hay datos disponibles
    print(tabulate(datos, headers='keys', tablefmt='grid'))