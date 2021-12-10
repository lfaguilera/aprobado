NOMBRE=0
CLAVE=1
FECHA = 0
HORA = 1

def leer(archivo):
    linea = archivo.readline()
    continuar=True
    registro="999999"
    if linea:
        registro = linea.rstrip().split(",")
    else:
        continuar=False
    return [registro,continuar]

def comparar_usuario(usuario):
    usuarios = open("datos_juego\\usuario.csv","r")
    existe=False
    mensaje=''
    usuario_registrado, continuar= leer(usuarios)
    while usuario!=usuario_registrado[NOMBRE] and (continuar == True) and (existe==False):
        usuario_registrado, continuar= leer(usuarios)
        if usuario==usuario_registrado[NOMBRE]:
            mensaje='El nombre de usuario ya existe ingrese otro'
            existe=True
            clave=usuario_registrado[CLAVE]
    lista=[existe,clave,mensaje]
    usuarios.close()
    return lista


def registrar_usuario(usuario,clave):
    #usuarios: nombre,clave
    NOMBRE=0
    CLAVE=1
    usuarios = open("datos_juego\\usuarios.csv","rw")
    usuarios.write(f'{usuario},{clave},0,0\n')

    usuarios.close()
    return
        
        

def validar_usuario_nuevo(usuario):

    regla = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    valido=True
    mensaje=''
    existe=False
    respuesta=[]
    usuarios = open("datos_juego\\usuarios.csv","r")
    usuario_registrado, continuar= leer(usuarios)
    
    if len(usuario)<4 or len(usuario)>15:
        mensaje="\nDebes escoger un nombre de entre 4 y 15 caracteres.\n¡Escoge otro"
        valido=False
    else:
        for caracter in usuario:
            if caracter not in regla:
                mensaje='Solo puedes incluir caracteres alfabéticos, numeros, y guiones en tu nombre.'
                valido=False

    while usuario!=usuario_registrado[NOMBRE] and (continuar == True) and (respuesta=='valido'):
        usuario_registrado, continuar= leer(usuarios)
        if usuario==usuario_registrado[NOMBRE]:
            mensaje='El nombre de usuario ya existe ingrese otro'
            valido=False
            existe=True
    
    respuesta=[valido,mensaje,existe]
    usuarios.close()
    return respuesta


def validar_clave(clave):
    regla = '-_aáqbcdeéfghiíjklmnoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNOÓPQRSTUÚVWXYZ0123456789'
    respuesta=''
    valido=0
    if len(clave)<=8 or len(clave)>=12:
        respuesta='La clave debe tener entre 8 y 12 caracteres'
    else:
        for caracter in clave:
            if caracter not in regla:
                respuesta='Solo puedes incluir caracteres alfabéticos, numeros, y guiones en tu clave.'
                   
    return respuesta

def ingresar(usuario,clave,puntos=0,turnos=0):
    existe,clave_real,mensaje=comparar_usuario(usuario)
    
    ingresa=False
    if existe and clave==clave_real: 
        ingresa=True

        
    return ingresa

def guardar_partida (jugadores,fin_partida):
    
    import os
    if os.stat("partidas_guardadas\\partidas.csv").st_size != 0:
        datos = open("partidas_guardadas\\partidas.csv","r")
        linea = datos.readline()
        datos_mod = open ("partidas_guardadas\\partidas_mod.csv","w") 
        contador = 0
        while linea and contador < len(jugadores.keys()):

            jugador = jugadores.keys()[contador]
            linea_anterior = linea.rstrip().split(',')
            linea_nueva = dic_csv(jugador,jugadores,fin_partida).rstrip().split(',')
            menor = min(linea_anterior[3],linea_nueva[3])
            if menor == linea_nueva :
                datos_mod.write(list_csv(linea_nueva))
                linea = datos.readline()
            else:
                datos_mod.write(list_csv(linea_anterior))
                contador += 1

    else:
        datos = open("partidas_guardadas\\partidas.csv","a")
        for jugador in jugadores.keys():
            linea = dic_csv(jugador,jugadores,fin_partida)
            datos.write(linea)
    
    datos.close()

def dic_csv (jugador,diccionario,fin_partida):
    aciertos = diccionario[jugador]['puntos']
    turnos = diccionario[jugador]['turnos']
    linea = f'{fin_partida[FECHA]},{fin_partida[HORA]},{jugador},{aciertos},{turnos}\n'
    return linea
    
def list_csv (lista):
    cadena = ""
    for dato in lista:
        if cadena == "":
            cadena += f'{dato}'
        else : 
            cadena += f',{dato}'
    cadena += "\n"
    return cadena

#guardar_partida({'juan': {'puntos': 100, 'turnos': 8}, 'pepe': {'puntos': 8, 'turnos': 8}, 'alberto': {'puntos': 5, 'turnos': 5}},["15/10/98","20:58"])