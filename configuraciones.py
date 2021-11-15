import time 
import random

def configurar_juego ():
    tiempo_inicio = time.time()
    fichas= int(input("\033[0;32m"+"\nCon cuantos pares de fichas desea jugar : "+"\033[0;m"))
    tablero = tablero_nuevo(fichas)
    #jugadores = defaultdict(lambda:{"puntos":0,"turnos":0})
    jugadores = {}
    jugadores = agregar_jugadores(jugadores)
    
    return tiempo_inicio , tablero , jugadores

def agregar_jugadores (jugadores):
    numero = int(input("\033[0;32m"+"Cual es el numero de jugadores : "+"\033[0;m"))
    for i in range(0,numero):
        color = random.randrange(31,37)
        jugador = str(input("Ingrese el nombre de jugador "+str(i+1)+" : "))
        jugadores[jugador] = {"puntos":0,"turnos":0,"color":color}
    #print (jugadores)
    return jugadores


def tablero_nuevo(numero_pares):
    tablero = []
    letras_usadas = ""
    while len(tablero) < numero_pares*2:
        letra_may = random.randrange(65 , 90 , step= 1)

        ficha = chr(letra_may)
        if ficha not in letras_usadas :
            letras_usadas += ficha
            tablero.append([ficha,0])
            tablero.append([ficha+"b",0])
    random.shuffle(tablero)
    #print(tablero)
    return tablero