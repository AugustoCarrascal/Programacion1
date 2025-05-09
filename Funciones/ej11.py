def contar_y_mostrar_primos (limite:int) -> int:
    cantidad_primos = 0

    print(f"numeros primos entre 1 y {limite}:")

    for numero in range (2, limite +1):
        es_primo = True

        for i in range(2,numero):
            if numero % i == 0:
                es_primo = False
                break

        if es_primo:
         print(numero)
         cantidad_primos += 1

    print (f"se encontraron {cantidad_primos} numeros primos.")
    return cantidad_primos
    
limite = int(input("Ingrese un numero: "))
contar_y_mostrar_primos(limite)
