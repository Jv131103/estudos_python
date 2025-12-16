def contagem(texto):
    d = {}

    for caracter in texto:
        d[caracter] = d.get(caracter, 0) + 1

    return d


texto = "banana"
d = contagem(texto)
print(d)
