def sumar_naturales(numero: int) -> int:
    if numero == 0:
        resultado = 0
    else:
        resultado = numero + (sumar_naturales(numero-1))
    return resultado

print(sumar_naturales(10))