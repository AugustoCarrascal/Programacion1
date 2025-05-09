import random
from juego import verificar_estado_partida,verificar_ganador_partida, verificar_ganador_ronda, mostrar_elemento

def jugar_piedra_papel_tijera() -> str:
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 1


    while ronda_actual <= 3:
        print(f"ronda actual: {ronda_actual}")

        jugador = int(input("elige 1 para piedra, 2 para papel, 3 para tijera: "))
        while jugador != 1 and jugador != 2 and jugador != 3:
            jugador = int(input("opcion invalida,elige 1 para piedra, 2 para papel, 3 para tijera: "))

  
        maquina = random.randint(1, 3)
    
        print("Jugador eligió:", mostrar_elemento(jugador))
        print("Maquina eligió:", mostrar_elemento(maquina))

        ganador = verificar_ganador_ronda(jugador, maquina)
      

        if ganador == "Jugador":
            aciertos_jugador += 1
        elif ganador == "Máquina":
            aciertos_maquina +=1

        print("El ganador de la ronda es:", ganador)
  
        if verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual) == False:
            break

        ronda_actual += 1

    ganador_partida = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    print("El ganador del juego es:", ganador_partida)

jugar_piedra_papel_tijera ()