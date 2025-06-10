def entero_maximo (lista:list)-> int:
    maximo = lista[0]
    posicion = 0
    for numero in range(len(lista)):
        if lista [numero] > maximo: 
            maximo = lista[numero]
            posicion = numero
    return posicion

lista = [4,10,15,30,40]
entero_maximo=entero_maximo(lista)
print ("la posicion del valor maximo es:",entero_maximo)
    
