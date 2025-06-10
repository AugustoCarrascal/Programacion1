#Implementar una función llamada reemplazar_nombres que reciba los siguientes parámetros:
#Una lista de nombres (lista_nombres).
#Un nombre a buscar en la lista (nombre_antiguo).
#Un nombre de reemplazo (nombre_nuevo).
#La función debe realizar las siguientes acciones:
#Reemplazar todas las apariciones de nombre_antiguo en lista_nombres por nombre_nuevo.
#Retornar la cantidad total de reemplazos realizados.

lista_nombres = ["roman", "martin", "guillermo", "carlos", "fernando"]
nombre_antiguo = "fernando" 
nombre_nuevo = "mariano"

def reemplazar_nombre(lista_nombres: list, nombre_antiguo: list, nombre_nuevo: list):
    
    cantidad_reemplazos = 0
    for i in range(len(lista_nombres)):
        if lista_nombres [i] == nombre_antiguo:
            lista_nombres [i] = nombre_nuevo
            cantidad_reemplazos +=1
    print(f"la cantidad de remplazos es: {cantidad_reemplazos}")
    return cantidad_reemplazos

reemplazar_nombre(lista_nombres, nombre_antiguo, nombre_nuevo)
