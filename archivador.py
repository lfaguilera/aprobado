import os

NOMBRE=0
CLAVE=1
FECHA = 0
HORA = 1
NOMBRE_USUARIO = 0
CLAVE_USUARIO = 1


def leer(archivo):
    """
    Alumno: Cerda Jose Antonio
    """
    linea = archivo.readline()
    continuar=True
    registro="999999"
    if linea:
        registro = linea.rstrip().split(",")
    else:
        continuar=False
    return [registro,continuar]

def leer_configuraciones ():
    """
    Alumno: Aguilera Luciano Fedrico
    """
    datos = open("datos_juego\\configuraciones.csv","r")
    
    datos.readline()
    linea = datos.readline()
    list_config = linea.rstrip("\n").split(",") if linea else [ 4, 2, 2, False ]
    
    datos.close()
    
    return list_config

def ingresar_usuario( usuario ):
    """
    Alumno: Cerda Jose Antonio
    """
    usuarios = open("datos_juego\\usuario.csv","r")
    existe=False

    usuario_registrado, continuar= leer(usuarios)
    
    while usuario != usuario_registrado [ NOMBRE ] and (continuar == True) and (existe == False):
        
        usuario_registrado, continuar= leer(usuarios)
        
        if usuario == usuario_registrado [ NOMBRE ]:
            existe = True
    
    respuesta = [ existe, usuario_registrado ]
    usuarios.close()

    return respuesta


def registrar_usuario(usuario,clave):
    """
    Alumno: Cerda Jose Antonio
    """
    #usuarios: nombre,clave
    NOMBRE=0
    CLAVE=1

    usuarios = open("datos_juego\\usuarios.csv","a")
    usuarios.write(f'{usuario},{clave}\n')

    usuarios.close()
    
    return
        
def chequear_usuario (usuario,clave):
    """
    Alumno: Aguilera Luciano Federico
     """
    usuario_valido = False
    usuarios_reg = open("datos_juego\\usuarios.csv","r")
    usuarios_reg.readline()
    linea = usuarios_reg.readline()
    
    while linea and not usuario_valido:
        linea = linea.rstrip("\n").split(",")
        
        if linea[NOMBRE_USUARIO] == usuario:
            usuario_valido = True
        
        else:
            linea = usuarios_reg.readline()

    if usuario_valido and clave == linea[CLAVE_USUARIO] :
        clave_valida = True

    else :
        clave_valida = False

    usuarios_reg.close()
    return usuario_valido, clave_valida

def validar_usuario_nuevo(usuario):
    """
    Alumno: Cerda Jose Antonio: La funcion valida una cadena de caracteres y devuelve una lista respuesta que:
    Su primer elemento es un booleano que indica si el string cumple o no las condiciones especidicadas.
    El segundo elemento es un mensaje destinado a ser mostrado en interfaz gráfica.
    Retorna la lista respuesta

    """
    usuario=str(usuario)
    regla = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    valido=True
    mensaje=''
    existe=False

    usuarios = open("datos_juego\\usuarios.csv","r")
    usuario_registrado, continuar= leer(usuarios)
    
    if not ( 4 < len( usuario) < 15 ):
        mensaje="Debes escoger un nombre de entre 4 y 15 caracteres.\n¡Escoge otro!"
        valido=False
    
    else:
    
        for caracter in usuario:
    
            if caracter not in regla:
    
                mensaje='Solo puedes incluir caracteres alfabéticos, numeros, y guiones en tu nombre.'
                valido=False
    
            else:
    
                valido==True

    while usuario!=usuario_registrado[NOMBRE] and (continuar == True) and (valido==True):
        usuario_registrado, continuar= leer(usuarios)
        if usuario==usuario_registrado[NOMBRE]:
            mensaje='El nombre de usuario ya existe ingrese otro'
            valido=False
            existe=True
    
    respuesta=[valido,mensaje,existe]
    usuarios.close()

    return respuesta


def validar_clave_nueva(clave):
    """
    Alumno: Cerda Jose Antonio: La función valida una cadena de caracteres y devuelve una lista respuesta que:
    Su primer elemento es un booleano que indica si el string cumple o no las condiciones especificadas.
    El segundo elemento es un mensaje destinado a ser mostrado en interfaz gráfica.
    Retorna la lista respuesta

    """
    clave=str(clave)
    regla = '-_aáqbcdeéfghiíjklmnoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNOÓPQRSTUÚVWXYZ0123456789'
    mensaje = ''
    valido = True

    if not ( 8 < len( clave) < 12 ):

        mensaje='La clave debe tener entre 8 y 12 caracteres'
        valido=False
    
    else:
    
        for caracter in clave:
    
            if caracter not in regla:
                mensaje='Solo puedes incluir caracteres alfabéticos, numeros, y guiones en tu clave.'
                valido = False
    
    respuesta=[valido,mensaje]              
    return respuesta


def guardar_partida (jugadores,fin_partida):
    """
    Alumno: Aguilera Luciano Federico
    """
    
    ord_jugadores = sorted(jugadores.items(),key=lambda x:x[1]['puntos'],reverse=True)
    
    datos = open("partidas_guardadas\\partidas.csv","r")
    datos_mod = open ("partidas_guardadas\\partidas_mod.csv","w")
    if os.stat("partidas_guardadas\\partidas.csv").st_size != 0:
        
        linea = datos.readline()
         
        ord_jugadores
        
        while linea and len(ord_jugadores)>0:

            
            linea_anterior = linea.rstrip().split(',')
            linea_nueva = dic_csv(ord_jugadores[0][0],jugadores,fin_partida).rstrip().split(',')
                
            if (int(linea_anterior[3]) <= int(linea_nueva[3])) and len(ord_jugadores)>0:
                datos_mod.write(list_csv(linea_nueva))
                ord_jugadores.pop(0)
                
            else:
                datos_mod.write(list_csv(linea_anterior))
                linea = datos.readline()
        
    else:
        
        datos = open("partidas_guardadas\\partidas.csv","a")
        
        for jugador in jugadores.keys():
        
            linea = dic_csv(jugador,jugadores,fin_partida)
            datos_mod.write(linea)
            
    
    datos.close()
    datos_mod.close()
    os.remove("partidas_guardadas\\partidas.csv")
    os.replace("partidas_guardadas\\partidas_mod.csv","partidas_guardadas\\partidas.csv")
    print("Puntajes guardados")


def dic_csv (jugador,dicc,fin_partida):
    """
    Alumno: Aguilera Luciano Federico
    """
    aciertos = dicc[jugador]['puntos']

    turnos = dicc[jugador]['turnos']
   
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

def reiniciar_partidas():
    with open("partidas_guardadas\\partidas.csv","w")as f:
        pass


def obtener_eleccion ():
    with open ("datos_juego\\continuar.txt","r") as eleccion :
        linea = eleccion.readline()
        if linea == "True" :
            continuar = True
        else:
            continuar = False
    return continuar