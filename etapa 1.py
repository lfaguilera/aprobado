import time
import random
from collections import defaultdict
from typing import DefaultDict

#memotest
def tablero_nuevo(numero_pares):
    tablero = []
    while len(tablero) < numero_pares*2:
        letra_may = random.randrange(65 , 90 , step= 1)

        ficha = chr(letra_may)
        if ficha not in tablero :
            tablero.append(ficha)
            tablero.append(ficha)
    random.shuffle(tablero, random.random)

    return tablero
    
def cuantos_jugadores():
    jugadores= defaultdict(lambda:{"puntos":0,"turnos":0})
    jugador=int(input("Cuantos jugadores?"))
    for i in range(0,jugador):
        jugadori=input("Ingrese nombre del jugador:")
        jugadores.append(jugadori)
    return jugadores

def tablero(mesa, posiciones):
    son_iguales = True
    vuelve=posiciones[:]
    while son_iguales==True:

        fichas=mesa
        print('Fichas y Posiciones: ',posiciones)
        print("Elija una ficha")
        opcion_1 = int(input('1er Posicion:'))
        posiciones[opcion_1-1] = fichas[opcion_1]
        print(posiciones)
        
        opcion_2 = int(input('2do Posicion:')) 
        posiciones[opcion_2-1] = fichas[opcion_2]
        print(posiciones)
    
        if posiciones[opcion_2-1]==posiciones[opcion_1-1]:
            son_iguales=True
            print("Muy bien podes seguir")
            posiciones[opcion_1-1]=posiciones[opcion_1-1]
            posiciones[opcion_2-1]=posiciones[opcion_2-1]
            print(posiciones)
        else:
            print("PROXIMO")
            son_iguales=False
            posiciones=vuelve
            
            
    return posiciones
    

def main():
    tiempo_inicio = time.time()
    mesa={}
    #[1,2,3,4]
    mesa=tablero_nuevo(2)
    jugadores=cuantos_jugadores()
    #posiciones=[1,2,3,4]
    ganador=False
    
    while ganador==False:
        for i in range(0,len(jugadores)):
            print("Es el turno de",jugadores[i])
            posiciones=tablero(mesa, posiciones)
    
    tiempo_final = time.time()
    print("El tiempo de la partida es ",tiempo_final-tiempo_inicio)
        
main()