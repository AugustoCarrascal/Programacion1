def tabla_multiplicar (numero: int, inicio: int = 1, fin: int = 10):
    print (f"tabla de multiplicar del numero {numero} ({inicio} a {fin}):")
    for i in range (inicio, fin +1):
        print (f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
inicio = int(input("Ingrese el valor de inicio (opcional, por defecto es 1): ") or 1)
fin = int(input("Ingrese el valor de fin (opcional, por defecto es 10): ") or 10)

tabla_multiplicar(numero, inicio, fin)