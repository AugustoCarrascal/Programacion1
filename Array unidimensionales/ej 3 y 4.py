def crear_array_enteros(numero: int) -> list:
    lista = [0] * numero
    for i in range(numero):
        valor = int(input("ingrese el numero: "))
        lista [i] = valor
    print (lista)
    return lista

def calcular_promedio (lista: list) -> float:
    promedio = 0
    if len (lista) > 0:
        suma = 0 
        for numero in lista:
            suma += numero
        promedio = suma / len(lista)
    print("El promedio es:", promedio)
    return promedio

def calcular_promedio_positivo (lista: list) -> float:
    suma_positiva = 0
    cantidad_positivos = 0
    for numero in lista:
        if numero > 0:
            suma_positiva += numero
            cantidad_positivos += 1
    if cantidad_positivos > 0:
        promedio_positivo = suma_positiva / cantidad_positivos
    else:
        promedio_positivo = 0
        print("no se ingresaron numeros positivos")
    print("el promedio de los positivos es: ",promedio_positivo)
    return promedio_positivo

numero = int(input("Ingrese la cantidad de enteros que desea ingresar: "))
mi_lista = crear_array_enteros(numero)
promedio = calcular_promedio(mi_lista)
promedio_positivo = calcular_promedio_positivo (mi_lista)
