#Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la intersección de los dos arrays.

def interseccion( listaA : list, listaB: list ) -> list:
    lista_interseccion = []
    for i in range(len(listaA)):
        for j in range(len(listaB)):
            if listaA[i] == listaB[j]:
                lista_interseccion = lista_interseccion + [listaA[i]]

    print(lista_interseccion)
    return lista_interseccion


listaA=[1,40,52,65,57]
listaB=[2,57,40,54]
interseccion (listaA,listaB)