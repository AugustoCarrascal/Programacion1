from validate import validate_length , validate_number

def get_int (mensaje : str, mensaje_error : str, minimo : int, maximo: int, reintentos : int) -> int | None:
    while reintentos > 0:
        entrada = input(mensaje)
        numero = int(entrada)

        if validate_number (numero, minimo, maximo):
            return numero
        else: 
            print (mensaje_error)
            reintentos -= 1
    return None 

numero_int = get_int ("ingrese un numero entre 1 y 10: ", "numero invalido", 1, 10, 3)

def get_float (mensaje : str, mensaje_error : str, minimo : float, maximo: float, reintentos : int) -> float | None:
    while reintentos > 0:
        entrada = input(mensaje)
        numero = float(entrada)
        numero_validado = validate_number (numero,minimo,maximo)
        retorno = None
        if numero_validado == numero:
            retorno = numero
            break
        else: 
            print (mensaje_error)
            reintentos -= 1
        retorno = None 
    return retorno

numero_decimal = get_float("ingrese un numero decimal entre 0.0 y 100.0: ", "numero invalido", 0.0, 100.0, 3)

def get_string ( longitud : int ) -> str | None: 
    reintentos = 3  
    while reintentos > 0:
        entrada = input(f"ingrese un texto (maximo {longitud} caracteres): ")

        if validate_length(entrada, longitud):
            return entrada
        else:
            print (f"error : el texto supera los {longitud} caracteres permitidos")
            reintentos -=1

    return None
    
texto = get_string (5)
