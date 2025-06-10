def productos_en_comun(lista1: list, lista2: list) -> list:
    lista_en_comun = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                repetido = False
                for k in range(len(lista_en_comun)):
                    if lista_en_comun[k] == lista1[i]:
                        repetido = True
                if repetido == False:
                    lista_en_comun = lista_en_comun + [lista1[i]]
    return lista_en_comun
   
def productos_exclusivos(lista1: list, lista2: list) -> list:
    lista_exclusivos = []
    for i in range(len(lista1)):
        encontrado_en_lista2 = False
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                encontrado_en_lista2 = True
                break

        if encontrado_en_lista2 == False:
            repetido = False
            for k in range(len(lista_exclusivos)):
                if lista_exclusivos[k] == lista1[i]:
                    repetido = True
                    break
            if repetido == False:
                lista_exclusivos += [lista1[i]]
    return lista_exclusivos


def catalogo_total(lista1: list, lista2: list) -> list: 
    catalogo = []
    for i in range(len(lista1)):
        repetido = False
        for j in range(len(catalogo)):
            if lista1[i] == catalogo[j]:
                repetido = True
                break
        if repetido == False:
            catalogo += [lista1[i]]

    for i in range(len(lista2)):
        repetido = False
        for j in range(len(catalogo)):
            if lista2[i] == catalogo[j]:
                repetido = True
                break
        if repetido == False:
            catalogo += [lista2[i]]
    
    return catalogo

def recomendaciones(usuario1: list, usuario2: list) -> None:
    recomendaciones_para_usuario1 = productos_exclusivos(usuario2, usuario1)
    recomendaciones_para_usuario2 = productos_exclusivos(usuario1, usuario2)

    print("🔁 Recomendaciones:")
    print("Para Usuario 1 recomendamos comprar los siguientes productos:", recomendaciones_para_usuario1)
    print("Para Usuario 2 recomendamos comprar los siguientes productos:", recomendaciones_para_usuario2)

