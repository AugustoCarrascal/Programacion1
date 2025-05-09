def cadena() -> int:
    texto = input("ingrese una cadena de texto: ")
    while not texto.strip():
        print ("error: la cadena no puede estar vacia.")
        texto = input ("ingrese una cadena de texto: ")
    return texto

