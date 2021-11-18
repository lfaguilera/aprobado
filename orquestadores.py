import os
from configuraciones import configurar_juego
from mecanicas_juego import juego
from mecanicas_juego import cronometro

def orquestador():
    """
    Luciano Federico Aguilera y Jose Cerda : Funcion principal del programa.
    """
    os.system('cls')
    #Se definen las variables globales necesarias
    pares = 0
    completo = False
    contador = 0
    #Se solicitan los valores para las opciones de juego.
    tiempo_0 , tablero , jugadores = configurar_juego()#importada de configuraciones.py
    lista_jugadores = list(jugadores.keys())

    while not completo :
        jugador = lista_jugadores[contador]
        #Presentamos al jugador de turno y el tablero actualizado
        print("\nEs el turno de ",f'\033[0;{jugadores[jugador]["color"]}m',jugador,"\033[0m","\n")
        completo , tablero , jugadores , pares = juego (tablero,jugador,jugadores , pares)#importada de mecanicas_juego.py
        jugadores[jugador]["turnos"] += 1
        if contador == len(lista_jugadores)-1 :
            contador = 0
        else :
            contador += 1

    ganador = lista_jugadores [0]
    for jugador in lista_jugadores :
        if jugadores[jugador]["puntos"] > jugadores[ganador]["puntos"] :
            ganador = jugador
    print ("El ganador fue ",ganador,"con ",jugadores[ganador]["puntos"]," puntos en ",jugadores[ganador]["turnos"],"turnos")
    
    #Una vez terminado el juego mostramos en pantalla la informacion de la partida
    tiempo = cronometro(tiempo_0)#importda de mecanicas_juego.py
    print("\033[0;32m"+"El tiempo que tomo la partida es ",tiempo,"\033[0;m")

