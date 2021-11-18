#Lucho: Función encargada de presentar el tablero actualizado en pantalla
def mostrar_tablero (tablero):
    fichas = ""
    numero = 1
    contador=0
    for ficha in tablero :
        if contador==4:
            fichas+="\n "
            contador=0
        if ficha[1] == 1 :
            fichas += ("["+ficha[0][0]+"]")
        else :
            
            fichas += "[" + str(numero) + "]"
        contador+=1
        numero += 1
    print(60*"*","\n\n","Fichas y posiciones :","\n",fichas,"\n\n"+60*"*")