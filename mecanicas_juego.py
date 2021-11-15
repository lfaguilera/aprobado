import time
from interfaz import mostrar_tablero

def cronometro (tiempo_inicio):
    tiempo_actual = time.time()
    tiempo_de_juego = tiempo_actual - tiempo_inicio
    if tiempo_de_juego > 60 :
        tiempo = str(round(tiempo_de_juego / 60,1)) + " minutos"
    else :
        tiempo = str(round(tiempo_de_juego,1)) + " segundos"
    return tiempo


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
                print (string)
                opcion = int(input())
                if  opcion > len(tablero)  or opcion <= 0  :
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