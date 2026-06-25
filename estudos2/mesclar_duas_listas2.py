def mesclar(lista1, lista2):
    if not lista1 and not lista2:
        return []

    i = 0
    j = 0

    novo = []
    while i < len(lista1) and j < len(lista2):
        novo.extend([lista1[i], lista2[i]])
        i += 1

    if i > len(lista1):
        novo.extend(lista1[i:])

    if j > len(lista2):
        novo.extend(lista2[j:])

    return novo


print(mesclar([1, 3, 5, 7], [2, 4, 6, 8]))
