import os
import csv
import sys
import time
import shutil
from datetime import date


lista_tareas = []

# Si no existe el archivo lo creamos
ruta_archivo = 'tareas.csv'

if os.path.exists(ruta_archivo):
    modo = 'r'

else:
    modo = 'a+'

# Leer el contenido del archivo y agregar a la lsita de tarear
with open(ruta_archivo, modo, newline='') as archivo_csv:

    contenido_archivo = csv.reader(archivo_csv, delimiter=';')

    for linea in contenido_archivo:
        lista_tareas.append(linea)

archivo_csv.close()

# print('Listado De Tareas\n')


def imprimir_lista_tareas():

    indice = 0

    for tarea in lista_tareas:
        # Calcular el estado de la tarea - if ternario
        estado = 'Completo' if tarea[2] == 'True' else 'Pendiente'

        # Leer el formato de fecha y convertirlo a un nuevo formato
        fecha = time.strptime(tarea[1], "%Y-%m-%d")

        nueva_fecha = time.strftime("%d/%m/%Y")

        # Imprimir los valores
        print(f"{indice + 1} {tarea[0]} {nueva_fecha} {estado}")

        indice += 1


def opcion_predeterminada():
    print("Opción inválida. Por favor, selecciona una opción válida.")

# Marcar tarea


def marcar_tarea():
    numero_tarea = int(
        input("Ingrese el número de la tarea que desea marcar: \n"))

    if numero_tarea < 0 or numero_tarea > len(lista_tareas):
        print('Opción incorrecta, debes ingresar el número de una tarea disponible')
    else:
        tarea = lista_tareas[numero_tarea - 1]

        if tarea[2] == 'True' or tarea[2] == 'Completo':
            print('La tarea ya se encuentra finalizada!!')
        else:
            tarea_actualizada = [tarea[0], tarea[1], 'True']
            lista_tareas[numero_tarea - 1] = tarea_actualizada

            # Crear nuevo archivo csv
            with open('temporal.csv', 'w+', newline='') as archivo_temporal:
                escritura = csv.writer(archivo_temporal, delimiter=';')
                escritura.writerows(lista_tareas)
                print(' LA TAREA SE COMPLETO CORRECTAMENTE!!')

            shutil.move(archivo_temporal.name, archivo_csv.name)

# Agregar Una Tarea Nueva


def agregar_tarea():
    nombre_tarea = input('¿Cómo se llama la tarea que deseas agrgar?\n')

    hoy = date.today()

    nueva_tarea = [nombre_tarea, hoy.isoformat(), 'False']

    lista_tareas.append(nueva_tarea)

    with open(ruta_archivo, 'a', newline='') as archivo_csv:
        contenido_nuevo = csv.writer(archivo_csv, delimiter=';')
        contenido_nuevo.writerow(nueva_tarea)
        print(' LA TAREA SE AGREGO CORRECTAMENTE!!')

    archivo_csv.close()


# Menu
while True:
    print("""
    ***** Que Desea Realizar *****
    1. Marcar tarea como completada
    2. Agregar nueva tarea
    3. Ver lista de tareas
    4. Salir
        """)

    seleccion = int(input("Elige una opción: "))

    match seleccion:
        case 1:
            imprimir_lista_tareas()
            marcar_tarea()
        case 2:
            agregar_tarea()
        case 3:
            print('Listado De Tareas\n')
            imprimir_lista_tareas()
        case 4:
            print("Saliendo del programa...")
            sys.exit()
        case _:
            opcion_predeterminada()
