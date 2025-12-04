def remover_duplicados(lista):
    novo = []

    for item in lista:
        if item not in novo:
            novo.append(item)

    return novo


print(remover_duplicados([1, 2, 1, 3, 2, 1, 4, 2]))
