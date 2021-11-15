import os
from configuraciones import configurar_juego
from mecanicas_juego import juego
from mecanicas_juego import cronometro


def orquestador():
    os.system('cls')
    pares = 0
    completo = False
    contador = 0
    tiempo_0 , tablero , jugadores = configurar_juego()
    lista_jugadores = list(jugadores.keys())
    while not completo :
        jugador = lista_jugadores[contador]
        print("\nEs el turno de ",f'\033[0;{jugadores[jugador]["color"]}m',jugador,"\033[0m","\n")
        completo , tablero , jugadores , pares = juego (tablero,jugador,jugadores , pares)
        if contador == len(lista_jugadores)-1 :
            contador = 0
        else :
            contador += 1
    
    
    tiempo = cronometro(tiempo_0)
    print("\033[0;32m"+"El tiempo que tomo la partida es ",tiempo,"\033[0;m")
    
def main ():
    orquestador()

main()