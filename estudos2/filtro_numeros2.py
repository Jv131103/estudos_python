def filtrar(lista):
    pos, neg, zeros = [], [], []

    for v in lista:
        if v > 0:
            pos.append(v)
        elif v < 0:
            neg.append(v)
        else:
            zeros.append(v)

    return {
        "positivos": pos,
        "negativos": neg,
        "zeros": zeros
    }


lista = [3, -1, 0, 12, -5, 8, 0, 7]
print(filtrar(lista))
