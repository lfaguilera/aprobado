import time
from interfaz import mostrar_tablero


def cronometro (tiempo_inicio):
    """
    Luciano Federico Aguilera: cronometro: retorna el tiempo que duro la partida, restando el tiempo de inicio de partida (que recibe como parametro) al tiempo actual."""
    tiempo_actual = time.time()
    tiempo_de_juego = tiempo_actual - tiempo_inicio
    #Según la duración de la partida se muestra en:
    #Minutos
    if tiempo_de_juego > 60 :
        tiempo = str(round(tiempo_de_juego / 60,1)) + " minutos"
    #Segundos
    else :
        tiempo = str(round(tiempo_de_juego,1)) + " segundos"
    
    return tiempo


def girar_ficha (primer_numero,segundo_numero, tablero, reset=False):
    """
    Luciano Federico Aguilera: La función recibe el tablero actualizado y dos numeros de fichas
    """ 
    #Ajustamos los valores seleccionados al rango de la lista
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
    """
    Luciano Federico Aguilera: La función controla que el numero corresponda a una posicion valida del tablero
    """
    valido = False
    while not valido :
            try  : 
                print (string)
                opcion = int(input())
                #Si el número no corresponde a una posicion
                if  opcion > len(tablero)  or opcion <= 0  :
                    print ("\033[0;31m"+"\nEl valor no corresponde a una posicion"+"\033[0m")
                #Si el número pertenece a una ficha que ya fue seleccionada o adivinada. 
                elif tablero[(opcion)-1][1]==1:
                    print("\033[0;31m"+"\nEL numero ya no esta disponible"+"\033[0m")
                else :
                    valido=True
            #Si se trata de un caracter no numérico
            except : 
                print ( "\033[0;31m"+"\nNo se trata de un valor numerico"+"\033[0m")
    return opcion 


def juego(tablero, jugador, jugadores , pares):
    """
    Luciano Federico Aguilera : La función juego:
    * Presenta al jugador de turno el tablero actualizado.
    * Solicita dos posiciones válidas del tablero.
    * En caso de acertar el par, suma puntos al jugador, y le permite seguir con el tablero actualizado.
    """
    #Flags para controlar la continuidad del turno o de la partida.
    completo = False
    pierde = False

    while (not completo) and (not pierde) :
        valido = False
        mostrar_tablero(tablero)#importada de interfaz.py

        print("Elija una ficha")
        #Se valida la posición seleccionada
        opcion_1 = validacion_numeros('\n1er Posicion:',tablero)#Función del archivo
        #De ser válida:
        tablero , par_igual = girar_ficha (opcion_1,0,tablero)#Función del archivo
        
        mostrar_tablero(tablero)
        #El programa procede de la misma manera con la segunda posición.
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