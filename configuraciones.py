import doctest
import random
from interfaz import interfaz_jugadores
from archivador import leer_configuraciones


CANTIDAD_FICHAS = 0


def agregar_jugadores ( nom_jugadores = [] ):
    """
    Alumno: Aguilera Luciano Fedrico: La función define un diccionarrio en base a la cantidad de jugadores y asigna sus nombres como clave.
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

def tablero_nuevo( test=False, prueba=1 ):
    """
    Alumno: Cerda Jose Antonio: La funcion recibe un numero n entero mayor o igual a 2 y menor a 24 que toma de el archivo configuracione.scv. 
    Retorna una lista con n pares unicos de listas que:
    En el primer elemento contienen la letra que representan. Si es el elemento par se concatena 'b'.
    El segundo elemento contiene un booleano.S
    >>> tablero_nuevo(True,4)
    [['A', False], ['Ab', False], ['B', False], ['Bb', False]]
    >>> tablero_nuevo(True,10)
    [['A', False], ['Ab', False], ['B', False], ['Bb', False], ['C', False], ['Cb', False], ['D', False], ['Db', False], ['E', False], ['Eb', False]]
    >>> tablero_nuevo(True,8)
    [['A', False], ['Ab', False], ['B', False], ['Bb', False], ['C', False], ['Cb', False], ['D', False], ['Db', False]]
    """
    
    tablero = []
    letras_usadas = ""
       
    if not test:
        config = leer_configuraciones()
        fichas = int(config[CANTIDAD_FICHAS])
        
    else :
        fichas = prueba
    
    
    if not (24 > fichas >=2) :
        fichas = 2
        
    letra = 65

    while len(tablero) < fichas or letra == 90:
        letra_may = letra
        ficha = chr(letra_may)
        letra +=1

        if ficha not in letras_usadas :

            letras_usadas += ficha
            tablero.append([ficha,False])
            tablero.append([ficha+"b",False])

    if not test:
        random.shuffle(tablero)
    
    return tablero

doctest.testmod()
    