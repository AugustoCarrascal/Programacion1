def calcular_fibonacci(numero: int) -> int:
    if numero == 0:
        resultado = 0        
    elif numero == 1:
        resultado = 1
    else:
        resultado = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

    return resultado

print(calcular_fibonacci(10))