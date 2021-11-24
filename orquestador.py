import os
import time

from configuraciones import agregar_jugadores
from configuraciones import tablero_nuevo
from mecanicas_juego import juego
from mecanicas_juego import cronometro


def orquestador():
    os.system('cls')
    #Se definen las variables globales necesarias para la finalizacion del juego
    pares = 0
    completo = False
    contador = 0
    #Se solicitan los valores para las opciones de juego.
    tablero = tablero_nuevo()#importada de configuraciones.py
    
    jugadores = agregar_jugadores ()#importada de configuraciones.py
    #Diccionario jugadores: jugadores[jugador] = {"puntos":0,"turnos":0,"color":color}
    lista_jugadores = list(jugadores.keys())
    #Se inicia el tiempo.
    tiempo_0 = time.time()

    while not completo :
        jugador = lista_jugadores[contador]

        #Presentamos al jugador de turno y el tablero actualizado
        print("\nEs el turno de ",f'\033[0;{jugadores[jugador]["color"]}m',jugador,"\033[0m","\n")
        #opcion_1=validar_opcion()
        #elegir_ficha(opcion_1)
        
        #girarficha() #importada de mecanicas_juego

        completo , tablero , jugadores , pares = juego (tablero,jugador,jugadores , pares)#importada de mecanicas_juego.py
        jugadores[jugador]["turnos"] += 1
        if contador == len(lista_jugadores)-1 :
            contador = 0
        else :
            contador += 1

    #Se define el ganador y se lo presenta
    ganador = lista_jugadores [0]
    for jugador in lista_jugadores :
        if jugadores[jugador]["puntos"] > jugadores[ganador]["puntos"] :
            ganador = jugador
    print ("El ganador fue ",ganador,"con ",jugadores[ganador]["puntos"]," puntos en ",jugadores[ganador]["turnos"],"turnos")
    
    #Una vez terminado el juego mostramos en pantalla la informacion de la partida
    tiempo = cronometro(tiempo_0)#importda de mecanicas_juego.py
    print("\033[0;32m"+"El tiempo que tomo la partida es ",tiempo,"\033[0;m")

