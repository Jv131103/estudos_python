def picos_da_lista(lista):
    picos = []
    for i in range(1, len(lista) - 1):
        if lista[i] > lista[i - 1] and lista[i] > lista[i + 1]:
            picos.append(lista[i])

    return picos


print(picos_da_lista([1, 3, 2, 5, 4, 10, 9]))
