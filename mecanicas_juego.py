import doctest 

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
    
    #por defecto las fichas elegidas no son iguales
    par_igual = False
    
    turno=[tablero,par_igual]

    mostrar_tablero(tablero)#import interfaz.py
            
    #opcion=input("Elija una ficha")
    print('Elija una ficha\n1er Posicion:')
    opcion_1 = validacion_numeros(tablero)
        
    turno = girar_ficha (opcion_1,0,tablero)

    mostrar_tablero(tablero)#import interfaz.py
    
    print('Elija una ficha\n2da Posicion:')
    opcion_2 = validacion_numeros(tablero)
            
    turno = girar_ficha(opcion_1,opcion_2,tablero)    

    return turno

def validacion_numeros (tablero,test=False) :
    """
    Luciano Federico Aguilera: La función controla que el numero corresponda a una posicion valida del tablero
    
    """
    valido = False
    while not valido :
            try  : 
                opcion = int(input("numero :"))
                #Si el número no corresponde a una posicion
                if  opcion > len(tablero)  or opcion <= 0  :
                    print ("\nEL numero no corresponde a una ficha")
                #Si el número pertenece a una ficha que ya fue seleccionada o adivinada. 
                elif tablero[(opcion)-1][1]==True:
                    print("\nEL numero ya no esta disponible")
                else :
                    valido=True
            #Si se trata de un caracter no numérico
            except : 
                print ( "\nNo se trata de un valor numerico")
    return opcion 


def girar_ficha (primer_numero,segundo_numero, tablero,test=False):
    """
    Luciano Federico Aguilera: La función recibe el tablero actualizado y dos numeros de fichas
    >>> girar_ficha (1,2,[['A', 0], ['J', 0], ['C', 1], ['D', 0], ['Cb', 1], ['Jb', 0], ['Db', 0], ['Ab', 0]],True)
    [[['A', 0], ['J', 0], ['C', 1], ['D', 0], ['Cb', 1], ['Jb', 0], ['Db', 0], ['Ab', 0]], False]
    >>> girar_ficha (1,8,[['A', 0], ['J', 0], ['C', 1], ['D', 0], ['Cb', 1], ['Jb', 0], ['Db', 0], ['Ab', 0]],True)
    [[['A', 1], ['J', 0], ['C', 1], ['D', 0], ['Cb', 1], ['Jb', 0], ['Db', 0], ['Ab', 1]], True]
    >>> girar_ficha (4,2,[['A', 0], ['J', 0], ['C', 1], ['D', 0], ['Cb', 1], ['Jb', 0], ['Db', 0], ['Ab', 0]],True)
    [[['A', 0], ['J', 0], ['C', 1], ['D', 0], ['Cb', 1], ['Jb', 0], ['Db', 0], ['Ab', 0]], False]
    """
    #Ajustamos los valores seleccionados al rango de la lista
    primer_numero += -1
    segundo_numero += -1
    par_igual = False
    #Cuando se recibe segundo parametro 0 se da vuelta la primera ficha
    if segundo_numero == -1 :
        tablero[primer_numero][1]= True

    #Sino se da vuelta la segunda ficha
    else:
        tablero[segundo_numero][1]=True
        
        #Si son iguales Letras
        if not (tablero[primer_numero][0][0] == tablero[segundo_numero][0][0]) or primer_numero == segundo_numero  :
            
            if primer_numero != segundo_numero :
                if not test:
                    print("\nLas fichas no coinciden") 
                    mostrar_tablero(tablero)
                
            tablero[primer_numero][1] = 0
            tablero[segundo_numero][1] = 0
            
        else :
            
            tablero[primer_numero][1] = 1
            tablero[segundo_numero][1] = 1
            if not test:
                mostrar_tablero(tablero)
            par_igual = True

    estado_tablero =[tablero , par_igual]

    return estado_tablero

def quien_gano(jugadores,lista_jugadores):
    """
    Jose Antonio Cerda: La función define quien gano el juego y lo presenta con sus respectivos puntos y turnos
    >>> quien_gano({"juan":{"puntos":0,"turnos":0,"color":0},"pepe":{"puntos":2,"turnos":1,"color":0}},["juan","pepe"])
    El ganador fue  pepe con  2  puntos en  1 turnos
    >>> quien_gano({"juan":{"puntos":3,"turnos":2,"color":0},"pepe":{"puntos":2,"turnos":1,"color":0}},["juan","pepe"])
    El ganador fue  juan con  3  puntos en  2 turnos
    >>> quien_gano({"juan":{"puntos":0,"turnos":0,"color":0},"pepe":{"puntos":5,"turnos":2,"color":0}},["juan","pepe"])
    El ganador fue  pepe con  5  puntos en  2 turnos
    """
    ganador = lista_jugadores[0]
    
    for jugador in lista_jugadores :
    
        if jugadores[jugador]["puntos"] > jugadores[ganador]["puntos"] :
    
            ganador = jugador
    
    print ("El ganador fue ",ganador,"con ",jugadores[ganador]["puntos"]," puntos en ",jugadores[ganador]["turnos"],"turnos")


doctest.testmod()

