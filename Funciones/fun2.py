def pedir_numero_float() -> float:
    entrada = input("Ingrese un número flotante: ")

    try:
        return float(entrada)
    except ValueError:
        print("Error: No es un número flotante válido.")
        return pedir_numero_float()

