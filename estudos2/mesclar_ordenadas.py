def mesclar_ordenadas(lista1, lista2):
    i = 0
    j = 0
    resultado = []

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    if i < len(lista1):
        resultado.extend(lista1[i:])
    elif j < len(lista2):
        resultado.extend(lista2[j:])

    return resultado


lista1 = [1, 4, 7, 10]
lista2 = [2, 3, 8, 12]
print(mesclar_ordenadas(lista1, lista2))

lista1 = [1, 2]
lista2 = [3, 4, 5, 6]
print(mesclar_ordenadas(lista1, lista2))

lista1 = []
lista2 = [1, 2, 3]
print(mesclar_ordenadas(lista1, lista2))

lista1 = [1, 3, 5]
lista2 = [1, 2, 5]
print(mesclar_ordenadas(lista1, lista2))
