def intercalar_listas(lista1, lista2):
    novo = []

    i = 0
    j = 0

    while i < len(lista1) and j < len(lista2):
        novo.append(lista1[i])
        novo.append(lista2[j])
        i += 1
        j += 1

    while i < len(lista1):
        novo.append(lista1[i])
        i += 1

    while j < len(lista2):
        novo.append(lista2[j])
        j += 1

    return novo


print(intercalar_listas([1, 2, 3], [10, 20, 30]))
print(intercalar_listas([1, 2], [10, 20, 30, 40]))
print(intercalar_listas([1, 2, 3], [10]))
