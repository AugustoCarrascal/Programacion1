def calcular_producto(lista: list) -> int:
    producto = 1
    for numero in lista:
        producto *= numero
    return producto

lista =  [2,3,4]
resultado = calcular_producto(lista)
print("el producto es: ",resultado)