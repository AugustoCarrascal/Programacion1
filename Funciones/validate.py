def validate_number(numero: int, minimo: int, maximo: int) -> int | float | None:
    if minimo <= numero <= maximo:  
        return numero  
    return None  

def validate_length(entrada: str, longitud_maxima: int) -> str | None:
    if len(entrada) <= longitud_maxima:  
        return entrada  
    return None