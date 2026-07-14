import math


def heuristica(origem, destino):
    x1, y1 = origem
    x2, y2 = destino

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


cidade = (2, 5)
destino = (10, 8)

print(heuristica(cidade, destino))
