def maior(lista):
    if not lista:
        return None

    m = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > m:
            m = lista[i]
    return m


print(maior([3, 1, 9, 2]))
