numero = int(input("ingrese numero: "))

if numero > 1:
    es_primo = True

    
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break  

    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} NO es un número primo.")
 