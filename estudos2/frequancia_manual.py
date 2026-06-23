def frequencia(lista):
    d = {}

    for valor in lista:
        d[valor] = d.get(valor, 0) + 1

    return d


def frequencia2(lista):
    d = {}

    for valor in lista:
        if valor in d:
            d[valor] += 1
        else:
            d[valor] = 1

    return d


print(frequencia(["a", "b", "a", "c", "b", "a"]))
print(frequencia2(["a", "b", "a", "c", "b", "a"]))
