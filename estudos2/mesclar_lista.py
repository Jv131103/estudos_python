def mesclar_listas(l1, l2):
    novo = []

    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        novo.append(l1[i])
        novo.append(l2[j])

        i += 1
        j += 1

    if i < len(l1):
        novo.extend(l1[i:])

    if j < len(l2):
        novo.extend(l2[j:])

    return novo


def mesclar_listas2(l1, l2):
    novo = []

    tam1 = len(l1)
    tam2 = len(l2)

    menor = tam1 if tam1 < tam2 else tam2

    for i in range(menor):
        novo.extend([l1[i], l2[i]])

    novo.extend(l1[menor:])
    novo.extend(l2[menor:])

    return novo


lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
print(mesclar_listas(lista1, lista2))
print(mesclar_listas2(lista1, lista2))

lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8, 9, 10]
print(mesclar_listas(lista1, lista2))
print(mesclar_listas2(lista1, lista2))
