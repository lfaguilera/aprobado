
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