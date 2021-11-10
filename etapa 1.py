import time
import random
from collections import defaultdict
import os
#memotest

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

def cronometro (tiempo_inicio):
    tiempo_actual = time.time()
    tiempo_de_juego = tiempo_actual - tiempo_inicio
    if tiempo_de_juego > 60 :
        tiempo = str(round(tiempo_de_juego / 60,1)) + " minutos"
    else :
        tiempo = str(round(tiempo_de_juego,1)) + " segundos"
    return tiempo

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

def girar_ficha (primer_numero,segundo_numero, tablero, reset=False):
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
            
    return tablero , par_igual

def validacion_numeros (string,tablero) :
    valido = False
    while not valido :
            try  : 
                opcion = int(input(f'{string} :'))
                if opcion > len(tablero) :
                    print ("\033[0;31m"+"\nEl valor no corresponde a una posicion"+"\033[0m")
                elif tablero[(opcion)-1][1]==1:
                    print("\033[0;31m"+"\nEL numero ya no esta disponible"+"\033[0m")
                else :
                    valido=True
            except : 
                print ( "\033[0;31m"+"\nNo se trata de un valor numerico"+"\033[0m")
    return opcion 


def juego(tablero, jugador, jugadores , pares):

    completo = False
    pierde = False

    while (not completo) and (not pierde) :
        valido = False
        mostrar_tablero(tablero)

        print("Elija una ficha")

        opcion_1 = validacion_numeros('\n1er Posicion:',tablero)
        tablero , par_igual = girar_ficha (opcion_1,0,tablero)
        
        mostrar_tablero(tablero)

        opcion_2 = validacion_numeros('\n2do Posicion:',tablero)
        tablero , par_igual = girar_ficha(opcion_1,opcion_2,tablero)
        
        if par_igual : 
            jugadores [jugador] ["puntos"] += 1 
            pares += 1
            
        else:
            pierde = True

            print("\nSiguiente jugador\n")
            jugadores[jugador]["turnos"] += 1

        if pares == int(len(tablero)/2) :
                print ("\033[0;31m"+"Fin del juego"+"\033[0m")
                completo = True
            



    return completo , tablero , jugadores , pares
    
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
    os.system('cls')
    pares = 0
    completo = False
    contador = 0
    tiempo_0 , tablero , jugadores = configurar_juego()
    lista_jugadores = list(jugadores.keys())
    while not completo :
        jugador = lista_jugadores[contador]
        print("\nEs el turno de ",f'\033[0;{jugadores[jugador]["color"]}m',jugador,"\033[0m","\n")
        completo , tablero , jugadores , pares = juego (tablero,jugador,jugadores , pares)
        if contador == len(lista_jugadores)-1 :
            contador = 0
        else :
            contador += 1
    
    
    tiempo = cronometro(tiempo_0)
    print("\033[0;32m"+"El tiempo que tomo la partida es ",tiempo,"\033[0;m")
    
        
main()