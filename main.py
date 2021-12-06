from orquestadores import orquestador
from ranking import rankear

def main (maximo=False):
    continuar = True
    while continuar and not maximo:
        jugadores = orquestador()
        continuar = rankear(jugadores)

main()