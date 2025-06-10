#Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.
def crear_array(numero: int|None) -> int:
    lista = [0] * numero
    print(lista)
    return (lista)

#Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.
def ingresar_numeros(cantidad: int) -> int:
    lista = crear_array(cantidad)
    for i in range (cantidad):
        numero = int(input(f"ingrese el numero: "))
        lista [i] = numero
    print (lista)
    return lista
    
cantidad = int(input("¿Cuántos números querés ingresar? "))
resultado = ingresar_numeros(cantidad)