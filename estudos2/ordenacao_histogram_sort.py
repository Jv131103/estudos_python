def histogram_sort(lista):

    hist = {}

    for valor in lista:
        hist[valor] = hist.get(valor, 0) + 1

    resultado = []

    for valor in sorted(hist):
        resultado.extend([valor] * hist[valor])

    return resultado


lista = [4, 2, 2, 8, 3, 3, 1]

print(histogram_sort(lista))
