
def mostrar_elemento(eleccion: int) -> str:
    if eleccion == 1:
        return "Piedra"
    elif eleccion == 2:
        return "Papel"
    elif eleccion == 3:
        return "Tijera"

def verificar_ganador_ronda(jugador: int, maquina: int) -> str:
    if jugador == 1 and maquina == 3:
        return "Jugador"
    elif jugador == 2 and maquina == 1:
        return "Jugador"
    elif jugador == 3 and maquina == 2:
        return "Jugador"
    
    elif jugador == 1 and maquina == 1:
        return "Empate"
    elif jugador == 2 and maquina == 2:
        return "Empate"
    elif jugador == 3 and maquina == 3:
        return "Empate"
    
    elif jugador == 1 and maquina == 2:
        return "Maquina"
    elif jugador == 2 and maquina == 3:
        return "Maquina"
    elif jugador == 3 and maquina == 1:
        return "Maquina"


def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int, ronda_actual: int) -> bool:
    if aciertos_jugador == 2 or aciertos_maquina == 2:
        return False
    if ronda_actual == 3:
        return False
    return True


def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int) -> str:
    if aciertos_jugador > aciertos_maquina:
        return "Jugador"
    elif aciertos_maquina > aciertos_jugador:
        return "Maquina"
    else:
        return "Empate"
