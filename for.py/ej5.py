suma = 0
contador = 0

for i in range (10):
    numero = int(input("ingrese un numero o (0 para salir): "))

    if numero == 0:
        break

    suma += numero
    contador +=1

if contador > 0:
    promedio = suma / contador
    print (f"suma total: {suma}")
    print (f"Promedio: {promedio}")
else:
    print ("no se ingresaron numeros validos")