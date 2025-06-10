#Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la diferencia de los dos arrays.
def diferencia(listaA:list, listaB:list) -> list:
    diferencia = []

    for i in range(len(listaA)):
        encontrado = False
        
        for j in range(len(listaB)):
            if listaA[i] == listaB[j]:
                encontrado = True
        
        if encontrado == False:
            diferencia = diferencia + [listaA[i]]

    print(diferencia)
    return diferencia


lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 6]
diferencia(lista1,lista2)