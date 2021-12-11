from orquestadores import orquestador
from ranking import rankear

def main (maximo=False):
    continuar = True
    while continuar and not maximo:
        jugadores,fin_partida = orquestador()
        continuar = rankear(jugadores,fin_partida)

main()