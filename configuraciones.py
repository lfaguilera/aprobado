import doctest

import random
from interfaz import interfaz_jugadores


def agregar_jugadores ():
    """
    Luciano Federico Aguilera: La función define un diccionarrio en base a la cantidad de jugadores y asigna sus nombres como clave.
    """
    jugadores={}
    nom_jugadores = interfaz_jugadores()
    
    for i in range(0,len(nom_jugadores)):
        color = random.randrange(31,37)
        jugador = nom_jugadores[i]
        jugadores[jugador] = {"puntos":0,"turnos":0,"color":color}


    return jugadores

def tablero_nuevo():
    """
    Jose Antonio Cerda: La funcion crea un tablero de n pares de fichas
    """
    tablero = []

    #Controla un unico par de fichas
    letras_usadas = ""
    valido = False

    while not valido :
        try :

            #Corroboramos el ingreso de un maximo de 23 pares y un minimo de 2
            fichas= int(input("\033[0;32m"+"\nCon cuantos pares de fichas desea jugar : "+"\033[0;m"))
            if 24 > fichas >=2 :
                valido = True
            else :
                print ("El valor ingresado es invalido , por favor ingrese otro")
        except:
            print("El valor ingresado no es un numero. Ingrese uno nuevo.")

    while len(tablero) < fichas*2:
        #Se obtiene un numero aleatorio a traves de la función randrange
        letra_may = random.randrange(65 , 90 , step= 1)
        #(Por código ASCII el intervalo [65,90] corresponde a letras mayúsculas)
        #Convertimos el valor a letra
        ficha = chr(letra_may)

        if ficha not in letras_usadas :

            letras_usadas += ficha
            #La primer posicion corresponde a la letra que contiene la ficha
            #La segunda posicion corresponde a un booleano que indica el estado de la ficha (cara arriba o cara abajo)
            tablero.append([ficha,False])
            #Se crea un par identico, salvo por su segundo caracter "p"
            tablero.append([ficha+"p",False])

    #Shuffle "mezcla" las letras en el tablero
    random.shuffle(tablero)
    
    return tablero