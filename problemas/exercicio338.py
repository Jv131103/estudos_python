def remover_duplicadas(lista):
    lista = sorted(lista)
    if not lista:
        return []

    novo = []

    i = 0
    j = 1

    novo.append(lista[i])
    while j < len(lista):
        if lista[i] != lista[j]:
            novo.append(lista[j])
        i += 1
        j += 1

    return novo


print(remover_duplicadas([1, 1, 2, 2, 3]))
