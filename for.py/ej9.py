#Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
numero = int(input("ingrese numero: "))
cantidad_divisores = 0
print (f"divisores de {numero}: ")
for i in range (1,numero +1):
    if numero % i == 0:
        print (i)
        cantidad_divisores +=1
print(f"la cantidad de divisores: {cantidad_divisores}")