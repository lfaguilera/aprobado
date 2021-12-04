from tkinter import Label, Tk , ttk, font
from PIL import ImageTk ,Image 

def terminar_partida (ventana):
    ventana.destroy()

def formato_ranking(jugadores,maximo_partidas):
    ventana_rk = Tk()
    ventana_rk.config(width=600,height=800)
    ventana_rk.title("MemoTest")
    ventana_rk.iconbitmap("icon.ico")

    img_corona =ImageTk.PhotoImage( Image.open("imagenes\\corona.png"))    
    oro = ImageTk.PhotoImage( Image.open("imagenes\\oro.png"))
    plata = ImageTk.PhotoImage( Image.open("imagenes\\plata.png"))
    bronce = ImageTk.PhotoImage( Image.open("imagenes\\bronce.png"))

    titulo = ttk.Label(ventana_rk,text="Ranking de jugadores :",font="Algerian")
    titulo.grid(column=1,row=0)
    imagen = Label(ventana_rk,image=img_corona)
    imagen.grid(column=0,row=0)
    nombre = Label (ventana_rk,text="Jugador",font="Algerian")
    nombre.grid(column=1,row=1)
    puntos = Label (ventana_rk,text="Puntaje",font="Algerian")
    puntos.grid(column=2,row=1)
    puntos = Label (ventana_rk,text="Intentos",font="Algerian")
    puntos.grid(column=3,row=1)
    puntos = Label (ventana_rk,text="Promedio Intentos",font="Algerian")
    puntos.grid(column=4,row=1)
    
    primer = Label(ventana_rk,image= oro )
    primer.grid(column=0,row=2)
    segundo = Label(ventana_rk,image=plata )
    segundo.grid(column=0,row=3)
    tercero = Label (ventana_rk,image= bronce )
    tercero.grid(column=0,row=4)
    
    fila = 1
    turnos=0
    jugadores_ord = sorted(jugadores.items(), key=lambda x: x[1]['puntos'], reverse=True)
    for jugador in jugadores_ord:
        fila +=1
        datos_jugador(fila,jugador,ventana_rk)
        turnos += jugador[1]['turnos']
    promedio_turnos=round(turnos/len(jugadores.keys()),1)
    promedio = Label(text=promedio_turnos,font="Cascadia 16")
    promedio.grid(column=4,row=2)

    eleccion_jugador(ventana_rk,maximo_partidas)
    
    ventana_rk.mainloop()

def datos_jugador(fila,jugador,ventana_rk):
    if fila == 2 :
        fondo = "#F1C40F"
    else:
        fondo = None
    jugador_puesto = Label(text=jugador[0],font="Cascadia 16",background=fondo)
    jugador_puesto.grid(column=1,row=fila)
    jugador_puntaje = Label(text=jugador[1]['puntos'],font="Cascadia 16")
    jugador_puntaje.grid(column=2,row=fila)
    jugador_puntaje = Label(text=jugador[1]['turnos'],font="Cascadia 16")
    jugador_puntaje.grid(column=3,row=fila)
    
    if fila > 4 :
        puesto_jugador = Label(text=str(fila-1),font="Cascadia 16")
        puesto_jugador.grid(column=0,row=fila)

def eleccion_jugador(ventana_rk,maximo_partidas):
    boton_fin = ttk.Button(ventana_rk,text="Terminar Juego",command=lambda :terminar_partida(ventana_rk))
    boton_fin.grid(column=4,rowspan=30)
    if not maximo_partidas :
        boton_repetir = ttk.Button(ventana_rk,text="Volver a jugar")
        boton_repetir.grid(column=4,rowspan=30)
    else :
        boton_repetir = Label(ventana_rk,text="Maximo de partidas alcanzado",background='red')
        boton_repetir.grid(column=4,rowspan=30)

def guardar_partida(jugadores):

    return 0

formato_ranking({'juan': {'puntos': 10, 'turnos': 3}, 'pepe': {'puntos': 5, 'turnos': 5},'Marley': {'puntos': 0, 'turnos': 1},'Barasi': {'puntos': 1, 'turnos': 8}, 'claudio': {'puntos': 3, 'turnos': 4}, 'pedro': {'puntos': 2, 'turnos': 7}},False)