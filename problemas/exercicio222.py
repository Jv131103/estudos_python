def mesclar(d1, d2):
    for chave, valor in d1.items():
        if chave not in d2:
            d2[chave] = valor
        else:
            d2[chave] += valor

    return d2


a = {"maçã": 3, "banana": 2, "uva": 5}
b = {"banana": 4, "pera": 3, "uva": 1}

print(mesclar(a, b))
