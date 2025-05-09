def maximo_numero(a,b,c) -> int:
    maximo = a 

    if b > maximo:
        maximo = b
    if c > maximo:
        maximo = c
    
    return maximo

resultado = maximo_numero(10,15,20)
print(f"el numero mas grande es: {resultado}")