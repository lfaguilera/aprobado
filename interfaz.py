from tkinter import Tk, ttk ,StringVar,Canvas

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
        if ficha[1] == 1 :
            fichas += ("["+ficha[0][0]+"]")
        else :
            
            fichas += "[" + str(numero) + "]"
        contador+=1
        numero += 1
    print(60*"*","\n\n","Fichas y posiciones :","\n",fichas,"\n\n"+60*"*")


def agregar (ventana , jugador, nom_jugador):
    
    if jugador != "" and jugador not in nom_jugador:
        aviso_jugador = ttk.Label(ventana,text=f'{jugador}',relief='solid',borderwidth=2,justify='left')
        aviso_jugador.grid(column=0)
        
        
        aviso = ttk.Label(ventana,text="Jugador agregado",background='green',relief='solid',borderwidth=2)
        aviso.grid(column=1,row=0)
        nom_jugador.append(jugador)
    else :
        aviso = ttk.Label(ventana,text=f' nombre invalido ',background= "red",relief='solid',borderwidth=2,)
        aviso.grid(column=1,row=0)
    return nom_jugador

def guardar_jugadores(ventana):
    ventana.destroy()


def interfaz_jugadores ():

    ventana = Tk()
    ventana.config(width=500,height=300)
    ventana.title("MemoTest")
    ventana.iconbitmap("icon.ico")
    ventana.minsize(height=200,width=300)
    
    var_nombre = StringVar()
    nom_jugadores = []
    entrada = ttk.Entry(ventana, textvariable=var_nombre)
    entrada.grid(column=0,row=0)
    
    boton_agregar = ttk.Button(ventana,text="Agregar nuevo jugador",command= lambda :agregar(ventana,var_nombre.get(),nom_jugadores) )
    boton_agregar.grid(column=0)
    boton_empezar = ttk.Button(ventana,text="Guardar jugadores",command=lambda: guardar_jugadores (ventana))
    boton_empezar.grid(column=0)
    jugadores_cargados = ttk.Label(ventana,text="Jugadores Ingresados :",justify='left')
    jugadores_cargados.grid(column=0,row=3)

    ventana.mainloop()
    
    return nom_jugadores
