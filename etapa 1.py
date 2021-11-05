import time
import random
from collections import defaultdict
from typing import DefaultDict

#memotest

def configurar_juego ():
    tiempo_inicio = time.time()
    fichas= int(input("Con cuantos pares de fichas desea jugar : "))
    tablero = tablero_nuevo(fichas)
    #jugadores = defaultdict(lambda:{"puntos":0,"turnos":0})
    jugadores = {}
    jugadores = agregar_jugadores(jugadores)
    
    return tiempo_inicio , tablero , jugadores

def agregar_jugadores (jugadores):
    numero = int(input("Cual es el numero de jugadores :"))
    for i in range(0,numero):
        jugador = str(input("Ingrese el nombre de jugador "+str(i+1)+" : "))
        jugadores[jugador] = {"puntos":0,"turnos":0}
    print (jugadores)
    return jugadores

def cronometro (tiempo_inicio):
    tiempo_actual = time.time()
    tiempo_de_juego = tiempo_actual - tiempo_inicio
    return tiempo_de_juego

def tablero_nuevo(numero_pares):
    tablero = []
    while len(tablero) < numero_pares*2:
        letra_may = random.randrange(65 , 90 , step= 1)

        ficha = chr(letra_may)
        if ficha not in tablero :
            tablero.append([ficha,0])
            tablero.append([ficha+"b",0])
    random.shuffle(tablero)
    print(tablero)
    return tablero

def girar_ficha (primer_numero,segundo_numero, tablero):

    par_igual = False

    if segundo_numero == 0 :
        tablero[primer_numero][1]= 1
        
    else:
        tablero[segundo_numero][1]=1
        mostrar_tablero(tablero)
        if not (tablero[primer_numero][0][0] == tablero[segundo_numero][0][0]) :
            tablero[primer_numero][1] = 0
            tablero[segundo_numero][1] = 0
        else :
            tablero[primer_numero][1] = 1
            tablero[segundo_numero][1] = 1
            par_igual = True
            
    return tablero , par_igual


def juego(tablero, jugador, jugadores):
    completo = False
    pares = 0
    pierde = False
    while not completo and not pierde :

        mostrar_tablero(tablero)

        print("Elija una ficha")

        opcion_1 = int(input('1er Posicion:'))
        tablero , par_igual = girar_ficha (opcion_1-1,0,tablero)
        
        mostrar_tablero(tablero)
        
        opcion_2 = int(input('2do Posicion:'))
        tablero , par_igual = girar_ficha(opcion_1-1,opcion_2-1,tablero)
        
        #mostrar_tablero(tablero)
    
        if par_igual : 
            jugadores [jugador] ["puntos"] += 1 
            pares += 1
            if pares == (len(tablero)/2) :
                completo = True
        else:
            pierde = True
            print("Siguiente jugador")
            jugadores[jugador]["turnos"] += 1
            
    return completo , tablero , jugadores
    
def mostrar_tablero (tablero):
    fichas = ""
    numero = 1
    for ficha in tablero :
        if ficha[1] == 1 :
            fichas += ("["+ficha[0][0]+"]")
        else :
            
            fichas += "[" + str(numero) + "]"
        numero += 1
    print(60*"*","\n\n","Fichas y posiciones :",fichas,"\n\n"+60*"*")

def main():
    completo = False
    tiempo_0 , tablero , jugadores = configurar_juego()
    while not completo :
        for jugador in jugadores.keys():
            print("Es el turno de ",jugador)
            completo , tablero , jugadores = juego (tablero,jugador,jugadores)
    
    tiempo = cronometro(tiempo_0)
    print("El tiempo que tomo la partida es ",tiempo,"segundos")
        
main()