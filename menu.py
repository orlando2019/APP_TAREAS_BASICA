import sys


def opcion_1():
    print("Has seleccionado la opción 1.")


def opcion_2():
    print("Has seleccionado la opción 2.")


def opcion_3():
    print("Has seleccionado la opción 3.")


def opcion_4():
    print("Has seleccionado la opción 4.")


def opcion_predeterminada():
    print("Opción inválida. Por favor, selecciona una opción válida.")


# def mostrar_menu():
#     print("MENU")
#     print("1. Opción 1")
#     print("2. Opción 2")
#     print("3. Opción 3")
#     print("4. Opción 4")
#     print("0. Salir")

# TODO: Otra forma de imprimi Valores
# print('{:>2} {:>20} {:>10} {:>10}'.format(
    #     indice + 1, tarea[0], nueva_fecha, estado))


while 1:
    print("""
        ***** Que Desea Realizar *****
        1. Opción 1
        2. Opción 2
        3. Opción 3
        4. Opción 4
        0. Salir
        """)
    seleccion = int(input("Elige una opción: "))

    match seleccion:
        case 1:
            opcion_1()
        case 2:
            opcion_2()
        case 3:
            opcion_3()
        case 4:
            opcion_4()
        case 0:
            print("Saliendo del programa...")
            sys.exit()
        case _:
            opcion_predeterminada()
