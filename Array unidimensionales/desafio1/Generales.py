from especificas import es_positivo, es_negativo, es_par, es_impar

def contar_positivos_negativos(lista: list) -> list:
    positivos = 0
    negativos = 0
    for i in range(len(lista)):
        if es_positivo(lista[i]):
            positivos += 1
        elif es_negativo(lista[i]):
            negativos += 1
    return [positivos, negativos]

def suma_pares(lista: list) -> int:
    suma = 0
    for i in range(len(lista)):
        if es_par(lista[i]):
            suma += lista[i]
    return suma

def mayor_impar(lista: list) -> int:
    mayor = lista[0]
    encontrado_impar = False

    for i in range(len(lista)):
        if es_impar(lista[i]):
            if encontrado_impar == False:
                mayor = lista[i]
                encontrado_impar = True
            else:
                if lista[i] > mayor:
                    mayor = lista[i]
    return mayor

def listar(lista: list) -> None:
    for i in range(len(lista)):
        print(lista[i])

def listar_pares(lista: list) -> None:
    for i in range(len(lista)):
        if es_par(lista[i]):
            print(lista[i])

def listar_posiciones_impares(lista: list) -> None:
    for i in range(len(lista)):
        if i % 2 != 0:
            print(lista[i])