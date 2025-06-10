#Crear una función que reciba como parámetros dos arrays. La función deberá mostrar la unión de los dos arrays.
def union(listaA: list, listaB: list) -> list:
    union = []
    union = listaA + listaB
    print (union)
    
listaA = [1,2,3]
listaB = [4,5,6]
union(listaA,listaB)