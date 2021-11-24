import random

#Jose: La función define un diccionario de diccionarios en base a la cantidad de jugadores y asigna sus nombres como clave.
def agregar_jugadores ():
    valido=False
    jugadores={}
    while not valido:
        try :
            numero = int(input("\033[0;32m"+"Cual es el numero de jugadores : "+"\033[0;m"))
            if numero > 0 and numero < 100:
                valido = True
            else :
                print ("El valor ingresado es invalido , por favor ingrese otro")
        except:
            print("El valor ingresado no es un numero. Ingrese uno nuevo.")    

    for i in range(0,numero):
        color = random.randrange(31,37)
        jugador = str(input("Ingrese el nombre de jugador "+str(i+1)+" : "))
        #Cada clave guarda un diccionario con información del jugador
        jugadores[jugador] = {"puntos":0,"turnos":0,"color":color}
    
    return jugadores

#Jose y Luciano: La función crea la lista tablero en base a un parametro entero
def tablero_nuevo():
    valido = False
    tablero = []
    while not valido :
        try :
            
            fichas= int(input("\033[0;32m"+"\nCon cuantos pares de fichas desea jugar : "+"\033[0;m"))
            if 24 > fichas >=2 :
                valido = True
            else :
                print ("El valor ingresado es invalido , por favor ingrese otro")
        except:
            print("El valor ingresado no es un numero. Ingrese uno nuevo.")
    #Variable para controlar pares únicos
    letras_usadas = ""
    while len(tablero) < fichas*2:
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
    print(type(tablero))
    print(tablero)
    print(tablero[0])
    
    return tablero