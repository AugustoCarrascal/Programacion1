def sumar_digitos (numero:int) -> int:
    if numero == 0:
        resultado = 0
    else:
        if numero > 0:
            resultado = numero + sumar_digitos (numero - 1)
        else:
            resultado = numero + sumar_digitos (numero + 1)
    return resultado

print(sumar_digitos(5))
print (sumar_digitos(-3))