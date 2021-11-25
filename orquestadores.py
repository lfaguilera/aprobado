import os
import time

from configuraciones import agregar_jugadores
from configuraciones import tablero_nuevo

from mecanicas_juego import cronometro, elegir_fichas
from mecanicas_juego import elegir_fichas
from mecanicas_juego import quien_gano


def orquestador():
    os.system('cls')

    #Variable necesaria para la finalizacion del juego
    completo = False
    
    pares = 0
    contador = 0
    
    tablero = tablero_nuevo()#importada de configuraciones.py
    jugadores = agregar_jugadores ()#importada de configuraciones.py

    lista_jugadores = list(jugadores.keys())
    
    tiempo_0 = time.time()

    while not completo:

        pierde=False

        #El contador nos indica el jugador de turno
        jugador = lista_jugadores[contador]
        
        #Presentamos al jugador de turno
        print("\nEs el turno de ",f'\033[0;{jugadores[jugador]["color"]}m',jugador,"\033[0m","\n")
        
        while not completo and not pierde:
            
            #El jugador elige las fichas del tablero
            tablero , par_igual = elegir_fichas(tablero)#import mecanicas_juego.py

            #Si acierta se le asignan los puntos, y se anota un par adivinado
            if par_igual : 
                jugadores [jugador] ["puntos"] += 1 
                pares += 1
            
            #De lo contrario se le suma el turno y se retorna al while principal
            else:
                pierde = True

                print("\nSiguiente jugador\n")
                jugadores[jugador]["turnos"] += 1

            #Si algun jugador adivina el ultimo par de fichas disponible el juego esta completo
            if pares == int(len(tablero)/2) :
                    print ("\033[0;31m"+"Fin del juego"+"\033[0m")
                    completo = True
        
        #Se controla el contador para la vuelta de turnos
        if contador == len(lista_jugadores)-1 :
            contador = 0
        else :
            contador += 1

    #Se define el ganador y se lo presenta
    quien_gano(jugadores,lista_jugadores)
    
    tiempo = cronometro(tiempo_0)#importda de mecanicas_juego.py
    print("\033[0;32m"+"El tiempo que tomo la partida es ",tiempo,"\033[0;m")

