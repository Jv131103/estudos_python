def agrupar_indices(lista):
    d = {}
    for idx, valor in enumerate(lista):
        if valor not in d:
            d[valor] = []
        d[valor].append(idx)

    return d


print(agrupar_indices([3, 7, 3, 2, 7, 7, 5]))
