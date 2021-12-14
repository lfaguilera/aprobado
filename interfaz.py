import doctest
from tkinter import Tk, ttk ,StringVar
from archivador import leer_configuraciones, validar_clave_nueva ,validar_usuario_nuevo, registrar_usuario, ingresar_usuario, chequear_usuario
import time
from archivador import leer_configuraciones



FUENTE =None
COLOR_OK='green'
COLOR_ERROR='red'
COLOR_MODIFICADO='orange'


CANTIDAD_FICHAS=0
MAXIMO_JUGADORES = 1
MAXIMO_PARTIDA=2
REINICIAR_ARCHIVO_PARTIDAS=3


def mostrar_tablero (tablero):
    """
    Alumnos: Aguilera Luciano Federico, Cerda Jose Antonio: Función encargada de presentar el tablero actualizado en pantalla
    
    """
    fichas = ""
    numero = 1
    contador=0
    
    for ficha in tablero :

        if contador==4:
            fichas+="\n "
            contador=0
        
        if ficha[1] == True :
            fichas += ("["+ficha[0][0]+"]")
        else :
            
            fichas += "[" + str(numero) + "]"
        contador+=1
        numero += 1

    print(60*"*","\n\n","Fichas y posiciones :","\n",fichas,"\n\n"+60*"*")

def interfaz_jugadores ():
    """
    Alumno : Aguilera Luciano Federico, Cerda Jose Antonio
    """
    ventana = Tk()
    ventana.config(width=500,height=300,background='#fff')
    ventana.title("MemoTest")
    ventana.iconbitmap("imagenes\\icon.ico")
    ventana.minsize(height=200,width=300)
    
    lista_configuraciones= leer_configuraciones()

    fichas_configuraciones=str(lista_configuraciones[0])
    jugadores_configuraciones=str(lista_configuraciones[1])
    maximo_configuraciones=str(lista_configuraciones[2])
    
    var_nombre = StringVar()
    var_clave = StringVar()

    nom_jugadores = []

    nombre = ttk.Label(ventana,text="Ingrese tu nombre de usuario:", justify='center',font=FUENTE)
    nombre.grid(column=0,row=0, padx=2,pady=2)

    entrada_nombre = ttk.Entry(ventana, textvariable = var_nombre, justify='center')
    entrada_nombre.grid(column=0,row=1, padx=1,pady=1)

    clave = ttk.Label(ventana,text="Ingrese tu clave:", justify='center',font=FUENTE)
    clave.grid(column=0,row=2, padx=2,pady=2)

    entrada_clave = ttk.Entry(ventana, textvariable = var_clave, justify='center')
    entrada_clave.grid(column=0,row=3, padx=1,pady=1)
    
    boton_ingresar = ttk.Button(ventana,text="Ingresar",command= lambda :ingresar(ventana,var_nombre.get(),var_clave.get(),nom_jugadores,entrada_nombre) )
    boton_ingresar.grid(column=0,row=4, padx=2,pady=4)
    
    boton_registrar = ttk.Button(ventana,text="Registrar Jugador",command= lambda :ventana_registrar_jugador())
    boton_registrar.grid(column=0,row=5, padx=2,pady=4)

    boton_comenzar = ttk.Button(ventana,text="Comenzar",command=lambda: comenzar (ventana,nom_jugadores))
    boton_comenzar.grid(column=0,row=6, padx=2,pady=4)

    jugadores_cargados = ttk.Label(ventana,text="Jugadores Ingresados",justify='left',font=FUENTE)
    jugadores_cargados.grid(column=1,row=1, padx=2,pady=2)

    mostrar_jugadores_cargados = ttk.Label(ventana,text=nom_jugadores,justify='left',font=FUENTE)
    mostrar_jugadores_cargados.grid(column=1,row=2, padx=2,pady=2)

    
    configuraciones_label = ttk.Label(ventana,text="Configuraciones:", justify='center',font=FUENTE, background='yellow')
    configuraciones_label.grid(column=3,row=0, padx=2,pady=2)
    
    config_fichas = ttk.Label(ventana, text = "Cantidad de fichas: "+fichas_configuraciones , font=FUENTE, foreground=COLOR_OK)
    config_fichas.grid(column=3,row=1,padx=2,pady=2)
    
    if fichas_configuraciones != '4':
        config_fichas.config(foreground=COLOR_MODIFICADO,text = "Cantidad de fichas: "+fichas_configuraciones+"- MODIFICADO")

    config_jugadores= ttk.Label(ventana, text = "Maximo de jugadores: "+jugadores_configuraciones, font=FUENTE, foreground=COLOR_OK)
    config_jugadores.grid(column=3,row=2,padx=2,pady=2)
    
    if jugadores_configuraciones != '2':
        config_jugadores.config(foreground=COLOR_MODIFICADO,text = "Maximo de jugadores: "+jugadores_configuraciones+"- MODIFICADO")

    maximo_partidas= ttk.Label(ventana, text = "Maximo de partidas: "+maximo_configuraciones, font=FUENTE, foreground=COLOR_OK)
    maximo_partidas.grid(column=3,row=3,padx=2,pady=2)
    
    if maximo_configuraciones != '2':
        maximo_partidas.config(foreground=COLOR_MODIFICADO,text = "Maximo de partidas: "+maximo_configuraciones+"- MODIFICAD")

    boton_reiniciar_archivo =  ttk.Button(ventana,text="REINICIAR ARCHIVO", font=FUENTE)
    boton_reiniciar_archivo.grid(column=3,row=4,padx=2,pady=2)

    ventana.mainloop()
    
    return nom_jugadores

doctest.testmod()

def ingresar (ventana , jugador, clave, nom_jugador, entrada):
    """
    Alumno : Aguilera Luciano Federico
    """
    #archivo=ingresar_usuario(jugador)
    usuario_valido, clave_valida =  chequear_usuario(jugador,clave)
    config = leer_configuraciones()
    maximo = int(config[MAXIMO_JUGADORES])
    
    if len(nom_jugador) < maximo:

        if jugador != "" and jugador not in nom_jugador and usuario_valido and clave_valida:
        
            aviso_jugador = ttk.Label(ventana,text=f'{jugador}',relief='solid',borderwidth=2,justify='center',font=FUENTE)
            aviso_jugador.grid(column=1)
            
            
            
            aviso = ttk.Label(ventana,text="     Jugador agregado      ",background='green',relief='solid',borderwidth=2,font=FUENTE)
            aviso.grid(column=1,row=0)
            nom_jugador.append(jugador)
        
        elif not usuario_valido  :
        
            aviso = ttk.Label(ventana,text=f' Usuario no registrado ',background= "red",relief='solid',borderwidth=2,font=FUENTE)
            aviso.grid(column=1,row=0)

        elif usuario_valido and not clave_valida :
    
            aviso = ttk.Label(ventana,text=f'La clave no corresponde',background= "red",relief='solid',borderwidth=2,font=FUENTE)
            aviso.grid(column=1,row=0)

        else :
            
            aviso = ttk.Label(ventana,text=f'   Usuario invalido    ',background= "red",relief='solid',borderwidth=2,font=FUENTE)
            aviso.grid(column=1,row=0)
    else :
        aviso = ttk.Label(ventana,text=f'  Maximo de jugadores  ',background= "red",relief='solid',borderwidth=2,font=FUENTE)
        aviso.grid(column=1,row=0)
    entrada.delete(0,'end')
    return nom_jugador

def comenzar(ventana,nom_jugadores):
    """
    Alumno : Aguilera Luciano Fedrico
    """
    if (len(nom_jugadores)>=2):

        ventana.destroy()
    else : 
        aviso = ttk.Label(ventana,text=f'El minimo son 2 jugadores',background= "red",relief='solid',borderwidth=2,font=FUENTE)
        aviso.grid(column=1,row=0)



def ventana_registrar_jugador():
    """
    Alumno : Cerda Jose Antonio
    """
    ventana_rg = Tk()
    ventana_rg.config(width=500,height=300)
    ventana_rg.title("MemoTest\REGISTRAR")
    ventana_rg.iconbitmap("imagenes\\icon.ico")
    ventana_rg.minsize(height=200,width=300)

    
    var_nombre = StringVar()
    var_clave = StringVar()
    var_clave_dos = StringVar()

    entrada_nombre = ttk.Entry(ventana_rg, textvariable = var_nombre,justify='center')
    entrada_nombre.grid(column=0,row=1)
    
    entrada_clave = ttk.Entry(ventana_rg,textvariable=var_clave,justify='center')
    entrada_clave.grid(column=0,row=3)

    entrada_clave_dos = ttk.Entry(ventana_rg, textvariable = var_clave_dos,justify='center')
    entrada_clave_dos.grid(column=0,row=5)

    
    nombre = ttk.Label(ventana_rg,text="Ingrese un nombre de usuario:", justify='center',font=FUENTE)
    nombre.grid(column=0,row=0)

    clave = ttk.Label(ventana_rg,text="Ingrese una clave:", justify='center',font=FUENTE)
    clave.grid(column=0,row=2)

    clave_dos = ttk.Label(ventana_rg,text="Reingrese la clave:", justify='center',font=FUENTE)
    clave_dos.grid(column=0,row=4)

    boton_registrar = ttk.Button(ventana_rg,text="Registrar", command= lambda :registrar_jugador(ventana_rg, entrada_nombre.get(), entrada_clave.get(), entrada_clave_dos.get() ))
    boton_registrar.grid(column=0)

def registrar_jugador (ventana_rg ,nombre, clave, clave_dos):
    """
    Alumno : Cerda Jose Antonio
    """
    nombre=str(nombre)
    clave=str(clave)
    clave_dos=str(clave_dos)

    aviso = ttk.Label(ventana_rg ,text='',font=FUENTE,relief='solid',borderwidth=2)
    aviso.grid(column=1,row=0)
    aviso_nombre = ttk.Label(ventana_rg ,text='',font=FUENTE,relief='solid',borderwidth=2)
    aviso_nombre.grid(column=1,row=1)
    aviso_clave = ttk.Label(ventana_rg ,text='',font=FUENTE)
    aviso_clave.grid(column=1,row=3)
    aviso_clave_dos = ttk.Label(ventana_rg ,text='',font=FUENTE)
    aviso_clave_dos.grid(column=1,row=5)

    respuesta_usuario = validar_usuario_nuevo(nombre)
    respuesta_clave = validar_clave_nueva(clave)

    if respuesta_usuario[0] == False:
        aviso_nombre.config(text=respuesta_usuario[1], background='red')
    
    else :
        aviso_nombre.config(text='¡Buen nombre!',background=COLOR_OK,relief='solid',borderwidth=2)

    if respuesta_clave[0] == False:
        aviso_clave.config(text=respuesta_clave[1],background=COLOR_ERROR,relief='solid',borderwidth=2)
        

    if clave_dos!=clave:
        aviso_clave_dos.config(text='¡Las claves no coinciden! Intenta nuevamente',background=COLOR_ERROR,relief='solid',borderwidth=2)
        
    if (respuesta_clave[0] == True) and (respuesta_usuario[0] == True) and (clave == clave_dos):    
     
        aviso.config(text='REGISTRADO',background=COLOR_OK,relief='solid',borderwidth=2)
        registrar_usuario(nombre,clave)
        time.sleep(2)
        ventana_rg.destroy()
    else:
        aviso.config(text='¡Uy! Algo no salió bien.',background=COLOR_ERROR,relief='solid',borderwidth=2)
     
    pass
