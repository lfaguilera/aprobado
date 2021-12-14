import os
import time
from tkinter import BooleanVar
from interfaz import mostrar_tablero
from configuraciones import agregar_jugadores, tablero_nuevo
from mecanicas_juego import cronometro, girar_ficha, quien_gano,validacion_numeros,registrar_partida
from ranking import rankear, tabla_final
from archivador import guardar_partida, leer_configuraciones

MAXIMO_PARTIDAS = 2


def orquestador():
    """
    Alumnos: Aguilera Luciano Fedrico, Cerda Jose Antionio: Funcion principal del programa
    """
    #Variables de control del juego
    contador = 0
    continuar = True

    config = leer_configuraciones()
    maximo_partidas = int(config[MAXIMO_PARTIDAS])    
    
    jugadores = agregar_jugadores()
    
    registro_jugadores={}
    
    while contador < maximo_partidas and continuar:
        #os.system('cls')
        
        #Variables de control de partidas
        turno = 0
        pares_encontrados = 0

        tablero = tablero_nuevo()
        tablero_completo = int( len( tablero) /2 ) 

        lista_jugadores = list( jugadores.keys() )
        #Variable que inicia el tiempo
        tiempo_0 = time.time()

        while pares_encontrados < tablero_completo:
        ######### CORTE DE CONTROL DE PARTIDA #####    
            
            pierde = False
            
            jugador_de_turno = lista_jugadores[turno]
            
            print("\nEs el turno de ",jugador_de_turno,"\n")
        
            while ( pares_encontrados < tablero_completo ) and not pierde:
            ################ CORTE DE CONTROL DE TURNO #################
                
                par_igual = False

                mostrar_tablero( tablero )
            
                print('Elija una ficha\n1er Posicion:')
                opcion_1 = validacion_numeros( tablero )
        
                tablero, par_igual = girar_ficha ( opcion_1, 0, tablero )

                mostrar_tablero(tablero)
    
                print('Elija una ficha\n2da Posicion:')
                opcion_2 = validacion_numeros(tablero)
            
                tablero, par_igual = girar_ficha(opcion_1,opcion_2,tablero)    

                if par_igual : 

                    jugadores [ jugador_de_turno ] [ "puntos" ] += 1 
                    pares_encontrados += 1
            
                else:

                    pierde = True
                    print("\nSiguiente jugador\n")
                
            jugadores [ jugador_de_turno ] [ "turnos" ] += 1
            
            if turno == len( lista_jugadores )-1 :
                turno = 0
            
            else :
                turno += 1


        fecha = time.strftime("%d/%m/%y")
        hora = time.strftime("%H:%M") 
        fin_partida = [ fecha, hora ]


        print ("\033[0;31m"+"Fin del juego"+"\033[0m")

        quien_gano( jugadores, lista_jugadores )
    
        tiempo = cronometro( tiempo_0 )
        
        print("\033[0;32m"+"El tiempo que tomo la partida es ",tiempo,"\033[0;m")

        guardar_partida(jugadores,fin_partida)

        
        
        contador += 1

        continuar = rankear( jugadores, fin_partida, maximo_partidas, contador ,continuar )

        jugadores, registro_jugadores = registrar_partida( jugadores, registro_jugadores )

        

    
    tabla_final ( registro_jugadores )
    