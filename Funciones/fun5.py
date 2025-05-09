import math 
def calcular_area_circulo (radio : float | int) -> float | None:
    resultado = None
    if type(radio) == float or type (radio) == int:
        resultado = math.pi * (radio ** 2)
        return resultado

print (calcular_area_circulo(1))
