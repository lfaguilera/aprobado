import doctest

import random
from interfaz import interfaz_jugadores
from archivador import leer_configuraciones
CANTIDAD_FICHAS = 0


def agregar_jugadores (nom_jugadores=[]):
    """
    Luciano Federico Aguilera: La función define un diccionarrio en base a la cantidad de jugadores y asigna sus nombres como clave.
    >>> agregar_jugadores (["juan","pepe","alberto"])
    {'juan': {'puntos': 0, 'turnos': 0}, 'pepe': {'puntos': 0, 'turnos': 0}, 'alberto': {'puntos': 0, 'turnos': 0}}
    >>> agregar_jugadores (["Roberto","Guido","Franco"])
    {'Roberto': {'puntos': 0, 'turnos': 0}, 'Guido': {'puntos': 0, 'turnos': 0}, 'Franco': {'puntos': 0, 'turnos': 0}}
    >>> agregar_jugadores (["Jose","Luciano","Albero","Juan","Maria"])
    {'Jose': {'puntos': 0, 'turnos': 0}, 'Luciano': {'puntos': 0, 'turnos': 0}, 'Albero': {'puntos': 0, 'turnos': 0}, 'Juan': {'puntos': 0, 'turnos': 0}, 'Maria': {'puntos': 0, 'turnos': 0}}
    """
    jugadores={}
    if len (nom_jugadores)<1:
        nom_jugadores = interfaz_jugadores()
    
    for i in range(0,len(nom_jugadores)):
        jugador = nom_jugadores[i]
        jugadores[jugador] = {"puntos":0,"turnos":0}


    return jugadores

def tablero_nuevo(test=False,prueba=1):
    """
    Jose Antonio Cerda: La funcion crea un tablero de n pares de fichas
    >>> tablero_nuevo(True,4)
    [['A', False], ['Ab', False], ['B', False], ['Bb', False]]
    >>> tablero_nuevo(True,10)
    [['A', False], ['Ab', False], ['B', False], ['Bb', False], ['C', False], ['Cb', False], ['D', False], ['Db', False], ['E', False], ['Eb', False]]
    >>> tablero_nuevo(True,8)
    [['A', False], ['Ab', False], ['B', False], ['Bb', False], ['C', False], ['Cb', False], ['D', False], ['Db', False]]
    """
    tablero = []

    #Controla un unico par de fichas
    letras_usadas = ""
    valido = False

    
        #Corroboramos el ingreso de un maximo de 23 pares y un minimo de 2
      
    if not test:
        config = leer_configuraciones()
        fichas = int(config[CANTIDAD_FICHAS])
        
    else :
        fichas = prueba
    if not (24 > fichas >=2) :
        fichas = 2

        
    letra = 65
    while len(tablero) < fichas or letra == 90:
        #Se obtiene un numero aleatorio a traves de la función randrange
        letra_may = letra
        #(Por código ASCII el intervalo [65,90] corresponde a letras mayúsculas)
        #Convertimos el valor a letra
        ficha = chr(letra_may)
        letra +=1

        if ficha not in letras_usadas :

            letras_usadas += ficha
            #La primer posicion corresponde a la letra que contiene la ficha
            #La segunda posicion corresponde a un booleano que indica el estado de la ficha (cara arriba o cara abajo)
            tablero.append([ficha,False])
            #Se crea un par identico, salvo por su segundo caracter "b"
            tablero.append([ficha+"b",False])

    #Shuffle "mezcla" las letras en el tablero
    if not test:
        random.shuffle(tablero)
    
    return tablero

doctest.testmod()