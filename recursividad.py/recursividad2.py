def potencia (base, exponente):
    if exponente == 0:
        resultado = 1 
    else:
        resultado = base * potencia (base, exponente - 1)
    return resultado

print(potencia(5,3))