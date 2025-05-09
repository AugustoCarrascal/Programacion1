def verificar_par(numero:int) -> bool:
    if numero % 2== 0:
        print (f"el numero {numero} es par ")
        return True
    else:
        print(f"el numero {numero} es impar ")
        return False

verificar_par(7)
verificar_par(10)