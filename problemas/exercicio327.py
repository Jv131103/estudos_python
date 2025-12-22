def frequencia(lista):
    d = {}
    for valor in lista:
        d[valor] = d.get(valor, 0) + 1

    return d


print(frequencia(["ana", "joão", "ana", "maria", "joão", "ana"]))
