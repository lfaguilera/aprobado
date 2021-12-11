import doctest
from tkinter import Tk, ttk ,StringVar
from archivador import validar_clave_nueva ,validar_usuario_nuevo, registrar_usuario, ingresar_usuario, chequear_usuario
import time

FUENTE =None

def mostrar_tablero (tablero):
    """
    Luciano Federico Aguilera y Jose Cerda: Función encargada de presentar el tablero actualizado en pantalla
    
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


def ventana_registrar_jugador():
    """
    Alumno : Cerda Jose
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
    Alumno : Cerda Jose
    """
    aviso = ttk.Label(ventana_rg ,text='',font=FUENTE)
    aviso.grid(column=1,row=1)
    aviso_clave = ttk.Label(ventana_rg ,text='',font=FUENTE)
    aviso_clave.grid(column=1,row=1)
    aviso_clave_dos = ttk.Label(ventana_rg ,text='',font=FUENTE)
    aviso_clave_dos.grid(column=1,row=1)

    aviso_clave = ''
    aviso_clave_dos = ''
    nombre=str(nombre)
    clave=str(clave)
    clave_dos=str(clave_dos)

    respuesta_usuario = validar_usuario_nuevo(nombre)
    respuesta_clave = validar_clave_nueva(clave)

    if respuesta_usuario[0] == False:
        aviso = ttk.Label(ventana_rg ,text=respuesta_usuario[1],background='red',relief='solid',borderwidth=2)
        aviso.grid(column=1,row=1)
    else :
        aviso = ttk.Label(ventana_rg ,text='¡Buen nombre!',background='green',relief='solid',borderwidth=2)
        aviso.grid(column=1,row=1)

    if respuesta_clave[0] == False:
        aviso_clave = ttk.Label(ventana_rg ,text=respuesta_clave[1],background='red',relief='solid',borderwidth=2)
        aviso_clave.grid(column=1,row=3)

    if clave_dos!=clave:
        aviso_clave_dos = ttk.Label(ventana_rg ,text='¡Las claves no coinciden! Intenta nuevamente',background='red',relief='solid',borderwidth=2)
        aviso_clave_dos.grid(column=1,row=5)

    if (respuesta_clave[0] == True) and (respuesta_usuario[0] == True) and (clave == clave_dos):    
     
        aviso = ttk.Label(ventana_rg ,text='REGISTRADO',background='green',relief='solid',borderwidth=2)
        aviso.grid(column=1,row=0)
        registrar_usuario(nombre,clave)
        time.sleep(2)
        ventana_rg.destroy()
    else:
        aviso = ttk.Label(ventana_rg ,text='¡Uy! Algo no salió bien.',background='red',relief='solid',borderwidth=2)
        aviso.grid(column=1,row=0)
        
      
    pass

def interfaz_jugadores ():
    """
    Alumno : Aguilera Luciano Federico
    """
    ventana = Tk()
    ventana.config(width=500,height=300)
    ventana.title("MemoTest")
    ventana.iconbitmap("imagenes\\icon.ico")
    ventana.minsize(height=200,width=300)
    
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
    boton_ingresar.grid(column=0,row=4, padx=2,pady=2)
    
    boton_registrar = ttk.Button(ventana,text="Registrar Jugador",command= lambda :ventana_registrar_jugador())
    boton_registrar.grid(column=0,row=5, padx=2,pady=2)

    boton_comenzar = ttk.Button(ventana,text="Comenzar",command=lambda: comenzar (ventana,nom_jugadores))
    boton_comenzar.grid(column=0,row=6, padx=2,pady=2)

    jugadores_cargados = ttk.Label(ventana,text="Jugadores Ingresados :",justify='left',font=FUENTE)
    jugadores_cargados.grid(column=1,row=1, padx=2,pady=2)

    ventana.mainloop()
    
    return nom_jugadores
doctest.testmod()

def ingresar (ventana , jugador, clave, nom_jugador, entrada):
    """
    Alumno : Aguilera Luciano Federico
    """
    
    #archivo=ingresar_usuario(jugador)
    usuario_valido, clave_valida =  chequear_usuario(jugador,clave)
    if jugador != "" and jugador not in nom_jugador and usuario_valido and clave_valida:
    
        aviso_jugador = ttk.Label(ventana,text=f'{jugador}',relief='solid',borderwidth=2,justify='center',font=FUENTE)
        aviso_jugador.grid(column=1)
        
        
        
        aviso = ttk.Label(ventana,text="   Jugador agregado    ",background='green',relief='solid',borderwidth=2,font=FUENTE)
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