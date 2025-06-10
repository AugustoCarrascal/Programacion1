from entrada import ingresar_datos
from Generales import *

lista_numeros = []
datos_ingresados = False

opcion = 0
while opcion != 8:
    print("1. Ingresar datos")
    print("2. Cantidad de positivos y negativos")
    print("3. Suma de números pares")
    print("4. Mayor número impar")
    print("5. Listar los números")
    print("6. Listar los números pares")
    print("7. Listar los números en posiciones impares")
    print("8. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        lista_numeros = ingresar_datos()
        datos_ingresados = True

    elif opcion >= 2 and opcion <= 7:
        if datos_ingresados == False:
            print("Debe ingresar los datos primero (opción 1).")
        else:
            if opcion == 2:
                resultado = contar_positivos_negativos(lista_numeros)
                print("Positivos:", resultado[0], " Negativos:", resultado[1])
            elif opcion == 3:
                print("Suma de pares:", suma_pares(lista_numeros))
            elif opcion == 4:
                print("Mayor impar:", mayor_impar(lista_numeros))
            elif opcion == 5:
                listar(lista_numeros)
            elif opcion == 6:
                listar_pares(lista_numeros)
            elif opcion == 7:
                listar_posiciones_impares(lista_numeros)

    elif opcion == 8:
        print("Saliendo del programa...")

    else:
        print("Opción inválida.")