import random
import os
import pandas as pd
import csv


# Función para crear un diccionario con valores aleatorios
def crear_diccionario(nombre, opciones):
    diccionario = {}
    for i in lista_generada:
        diccionario[i] = random.choice(opciones)
    return diccionario

# Diccionario global para almacenar los diccionarios creados
diccionarios_guardados = {}

while True:
    # Solicitar lista de id al usuario
    muestra = input("Número de muestra: ")
    lista_generada = list(range(1, int(muestra) + 1))

    # Solicitar entrada al usuario
    nombre_variable = input("Introduce el nombre de la variable: ")

    esRango = input("Es un rango numérico? (si/no): ")
    if esRango == "si":
        minimo = int(input("Introduce el valor mínimo: "))
        maximo = int(input("Introduce el valor máximo: "))
        lista_opciones = list(range(minimo, maximo + 1))
    else:
        opciones = input("Introduce las opciones de la variable, separadas por comas: ")
        lista_opciones = opciones.split(',')
    
    # Crear el diccionario usando la función
    nuevo_diccionario = crear_diccionario(nombre_variable, lista_opciones)
    
    # Guardar el diccionario en el diccionario global
    diccionarios_guardados[nombre_variable] = nuevo_diccionario
    
    # Imprimir el diccionario guardado
    print(f"Diccionario guardado en '{nombre_variable}':")
    print(nuevo_diccionario)
    
    # Preguntar al usuario si desea continuar
    continuar = input("¿Deseas agregar otro diccionario? (si/no): ").strip().lower()
    if continuar != 'si':
        break


# Crear una ruta relativa para el archivo CSV
directorio_actual = os.path.dirname(__file__)
archivo_csv = os.path.join(directorio_actual, 'datos_generados.csv')

with open(archivo_csv, mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir la primera fila con los nombres de las variables
    nombres_variables = ['id'] + list(diccionarios_guardados.keys())
    escritor_csv.writerow(nombres_variables)
    
    # Escribir las filas con los datos
    for i in lista_generada:
        fila = [i]
        for diccionario in diccionarios_guardados.values():
            fila.append(diccionario.get(i))
        escritor_csv.writerow(fila)

print("Archivo 'datos_generados.csv' creado exitosamente.")

# Ruta del archivo CSV
archivo_csv = 'datos_generados.csv'

# Ruta del archivo Excel a crear
archivo_excel = os.path.join(directorio_actual, 'datosGenerados.xlsx')

# Leer el archivo CSV en un DataFrame de pandas
df = pd.read_csv(archivo_csv)

# Guardar el DataFrame en un archivo Excel
df.to_excel(archivo_excel, index=False, engine='openpyxl')

print(f"Archivo CSV '{archivo_csv}' convertido a Excel y guardado como '{archivo_excel}'.")

input("presiona enter para salir")