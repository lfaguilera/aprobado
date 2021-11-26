import os
import time

from configuraciones import agregar_jugadores, tablero_nuevo

from mecanicas_juego import cronometro, elegir_fichas, quien_gano


def orquestador():
    os.system('cls')

    #Variables necesaria para la finalizacion del juego
    pares_encontrados = 0
    #Variable para contar los turnos de los jugadores
    turno = 0

    tablero = tablero_nuevo()#importada de configuraciones.py
    #Con el tablero definido podemos determinar cuando el juego esta completo
    completo = int(len(tablero)/2) 
    
    jugadores = agregar_jugadores ()#importada de configuraciones.py
    #Lista para controlar los turnos
    lista_jugadores = list(jugadores.keys())
    
    #inicia el tiempo
    tiempo_0 = time.time()

    ###CORTE DE CONTROL###
    while pares_encontrados < completo:
        
        jugador_de_turno = lista_jugadores[turno]
        #Por defecto el jugador no adivino pares
        pierde=False
        print("\nEs el turno de ",f'\033[0;{jugadores[jugador_de_turno]["color"]}m',jugador_de_turno,"\033[0m","\n")
        
        #CORTE DE CONTROL: Si no acierta el par pierde el turno
        while (pares_encontrados < completo) and not pierde:
            
            #El jugador elige las fichas del tablero
            tablero , par_igual = elegir_fichas(tablero)#import mecanicas_juego.py

            #Si acierta se le asignan los puntos, y se anota un par adivinado. El jugador continua jugando.
            if par_igual : 
                jugadores [jugador_de_turno] ["puntos"] += 1 
                pares_encontrados += 1
            
            else:
                pierde = True
    
        ###FINALIZA EL TURNO###
        
        jugadores[jugador_de_turno]["turnos"] += 1
        #Se controla el contador para la vuelta de turnos
        if turno == len(lista_jugadores)-1 :
            turno = 0
        else :
            turno += 1
        print("\nSiguiente jugador\n")

    ###FINALIZA EL JUEGO###
    
    print ("\033[0;31m"+"Fin del juego"+"\033[0m")

    #Se define el ganador y se lo presenta
    quien_gano(jugadores,lista_jugadores)
    
    tiempo = cronometro(tiempo_0)#importda de mecanicas_juego.py
    print("\033[0;32m"+"El tiempo que tomo la partida es ",tiempo,"\033[0;m")

