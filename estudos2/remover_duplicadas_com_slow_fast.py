def remover_duplicadas(lista):
    slow = 0

    for fast in range(1, len(lista)):
        if lista[slow] != lista[fast]:
            slow += 1
            lista[slow] = lista[fast]

    del lista[slow + 1:]
    return lista


lista = [1, 1, 2, 2, 2, 3, 5, 5]
print(remover_duplicadas(lista))
