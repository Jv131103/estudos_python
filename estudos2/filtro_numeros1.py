def filtrar(lista):
    positivos = [v for v in lista if v > 0]
    negativos = [v for v in lista if v < 0]
    zeros = [v for v in lista if v == 0]

    return {
        "positivos": positivos,
        "negativos": negativos,
        "zeros": zeros
    }


lista = [3, -1, 0, 12, -5, 8, 0, 7]
print(filtrar(lista))
