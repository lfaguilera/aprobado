import time
from interfaz import mostrar_tablero


def cronometro (tiempo_inicio):
    """
    Luciano Federico Aguilera: cronometro: retorna el tiempo que duro la partida, restando el tiempo de inicio de partida (que recibe como parametro) al tiempo actual."""
    tiempo_actual = time.time()
    tiempo_de_juego = tiempo_actual - tiempo_inicio
    
    #Según la duración de la partida se muestra en:
    if tiempo_de_juego > 60 :
        tiempo = str(round(tiempo_de_juego / 60,1)) + " minutos"
    #Segundos
    else :
        tiempo = str(round(tiempo_de_juego,1)) + " segundos"
    
    return tiempo

def elegir_fichas(tablero):
    
    turno=[]

    par_igual = False
    
    mostrar_tablero(tablero)#import interfaz.py
            
    print("Elija una ficha")
        
    opcion_1 = validacion_numeros('\n1er Posicion:',tablero)
        
    tablero , par_igual = girar_ficha (opcion_1,0,tablero)

    mostrar_tablero(tablero)#import interfaz.py

    opcion_2 = validacion_numeros('\n2do Posicion:',tablero)
            
    tablero , par_igual = girar_ficha(opcion_1,opcion_2,tablero)

    turno=[tablero,par_igual]    

    return turno

def validacion_numeros (string,tablero) :
    """
    Luciano Federico Aguilera: La función controla que el numero corresponda a una posicion valida del tablero
    """
    
    valido = False
    while not valido :
            try  : 
                print (string)
                opcion = int(input())
                #Si el número no corresponde a una posicion
                if  opcion > len(tablero)  or opcion <= 0  :
                    print ("\033[0;31m"+"\nEl valor no corresponde a una posicion"+"\033[0m")
                #Si el número pertenece a una ficha que ya fue seleccionada o adivinada. 
                elif tablero[(opcion)-1][1]==1:
                    print("\033[0;31m"+"\nEL numero ya no esta disponible"+"\033[0m")
                else :
                    valido=True
            #Si se trata de un caracter no numérico
            except : 
                print ( "\033[0;31m"+"\nNo se trata de un valor numerico"+"\033[0m")
    return opcion 

def girar_ficha (primer_numero,segundo_numero, tablero, reset=False):
    """
    Luciano Federico Aguilera: La función recibe el tablero actualizado y dos numeros de fichas
    """ 
    #Ajustamos los valores seleccionados al rango de la lista
    primer_numero += -1
    segundo_numero += -1
    par_igual = False

    if segundo_numero == -1 :
        tablero[primer_numero][1]= 1
        
    else:
        tablero[segundo_numero][1]=1
        
        if not (tablero[primer_numero][0][0] == tablero[segundo_numero][0][0]) or primer_numero == segundo_numero  :
            if primer_numero != segundo_numero :
                print("\033[0;31m"+"\nLas fichas no coinciden"+"\033[0m") 
                mostrar_tablero(tablero)
                
            tablero[primer_numero][1] = 0
            tablero[segundo_numero][1] = 0
            
        else :
            
            tablero[primer_numero][1] = 1
            tablero[segundo_numero][1] = 1
            mostrar_tablero(tablero)
            par_igual = True

    estado_tablero =[tablero , par_igual]

    return estado_tablero

def quien_gano(jugadores,lista_jugadores):
    """
    Jose Antonio Cerda: La función define quien gano el juego y lo presenta con sus respectivos puntos y turnos
    """
    
    ganador = lista_jugadores[0]
    
    for jugador in lista_jugadores :
    
        if jugadores[jugador]["puntos"] > jugadores[ganador]["puntos"] :
    
            ganador = jugador
    
    print ("El ganador fue ",ganador,"con ",jugadores[ganador]["puntos"]," puntos en ",jugadores[ganador]["turnos"],"turnos")