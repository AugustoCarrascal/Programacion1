def ingresar_datos() -> list:
    lista = []
    while len(lista) < 10:
        n = int(input("ingrese un numero entre -1000 y 1000: "))
        if -1000 <= n <= 1000:
            lista = lista + [n]
        else:
            print("numero de fuera de rango. intente de nuevo")
    print (lista)
    return lista

