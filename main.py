from tkinter import BooleanVar
from orquestadores import orquestador
from ranking import rankear
from archivador import leer_configuraciones
MAXIMO_PARTIDAS = 2

def main ():
    contador = 0
    continuar = True
    config = leer_configuraciones()
    maximo = config[MAXIMO_PARTIDAS]
    while contador != maximo and continuar:
        jugadores,fin_partida = orquestador()
        continuar = rankear(jugadores,fin_partida)
        
        
main()