import time 
import random
from interfaz import interfaz_jugadores


def configurar_juego ():
    """
    Luciano Federico Aguilera y Jose Cerda : La función define las variables para las opciones de juego.
    Utiliza dos funciones definidas en este archivo
    """
    valido = False
    while not valido :
        try :
            fichas= int(input("\033[0;32m"+"\nCon cuantos pares de fichas desea jugar : "+"\033[0;m"))
            if 24 > fichas >=2 :
                valido = True
            else:
                print ("El valor ingresado es invalido , por favor ingrese otro")
        except :
            print ("El valor ingresado es invalido , por favor ingrese otro")
    tablero = tablero_nuevo(fichas)

    
    jugadores = {}
    jugadores = agregar_jugadores(jugadores)
    
    #Se inicia el tiempo.
    tiempo_inicio = time.time()
    
    return tiempo_inicio , tablero , jugadores


def agregar_jugadores (jugadores):
    """
    Luciano Federico Aguilera: La función define un diccionarrio en base a la cantidad de jugadores y asigna sus nombres como clave.
    """
    nom_jugadores = interfaz_jugadores()
    numero = len(nom_jugadores)
    
    for i in range(0,numero):
        color = random.randrange(31,37)
        jugador = nom_jugadores[i]
        jugadores[jugador] = {"puntos":0,"turnos":0,"color":color}


    return jugadores


def tablero_nuevo(numero_pares):
    """
    Luciano Federico Aguilera: La función crea la lista tablero en base a un parametro entero
    """
    tablero = []
    #Variable para controlar pares únicos
    letras_usadas = ""
    while len(tablero) < numero_pares*2:
        #Se obtiene un numero aleatorio a traves de la función randrange
        letra_may = random.randrange(65 , 90 , step= 1)
        #(Por código ASCII el intervalo [65,90] corresponde a letras mayúsculas)
        #Convertimos el valor a letra
        ficha = chr(letra_may)
        if ficha not in letras_usadas :
            letras_usadas += ficha
            tablero.append([ficha,0])
            tablero.append([ficha+"b",0])
    #Shuffle "mezcla" las letras en el tablero
    random.shuffle(tablero)
    #print(tablero)
    return tablero