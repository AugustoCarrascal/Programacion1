def entero_maximo (lista:list)-> int:
    maximo = lista[0]
    posicion = []
    for numero in range(len(lista)):
        if lista [numero] > maximo: 
            maximo = lista[numero]
            posicion =[numero]
        elif lista [numero] == maximo:
            posicion += [numero]
    return posicion

lista = [4,10,15,30,40,40,40]
entero_maximo = entero_maximo(lista)
print ("la posicion del valor maximo es:",entero_maximo)