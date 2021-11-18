import time 
import random

#Lucho: La función define las variables para las opciones de juego.
# Utiliza dos funciones definidas en este archivo
def configurar_juego ():
    fichas= int(input("\033[0;32m"+"\nCon cuantos pares de fichas desea jugar : "+"\033[0;m"))
    tablero = tablero_nuevo(fichas)
    #configurar_juego= []
    
    jugadores = {}
    jugadores = agregar_jugadores(jugadores)
    
    #Se inicia el tiempo.
    tiempo_inicio = time.time()
    
    return tiempo_inicio , tablero , jugadores

#Lucho: La función define un diccionarrio en base a la cantidad de jugadores y asigna sus nombres como clave.
def agregar_jugadores (jugadores):
    numero = int(input("\033[0;32m"+"Cual es el numero de jugadores : "+"\033[0;m"))
    for i in range(0,numero):
        color = random.randrange(31,37)
        jugador = str(input("Ingrese el nombre de jugador "+str(i+1)+" : "))
        jugadores[jugador] = {"puntos":0,"turnos":0,"color":color}
    
    return jugadores

#Lucho: La función crea la lista tablero en base a un parametro entero
def tablero_nuevo(numero_pares):
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