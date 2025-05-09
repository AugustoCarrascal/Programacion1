def es_primo(numero:int) -> bool:
    if numero < 2:
        return False
    
    for i in range (2,numero):
        if numero % i == 0:
            return False
        
    return True

numero = 17
if es_primo (numero):
    print (f"{numero} es primo")
else:
    print (f"{numero} no es primo")