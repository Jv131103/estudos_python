def remover_duplicadas(lista):
    lista = sorted(lista)
    if not lista:
        return []

    novo = [lista[0]]
    i = 0

    for j in range(1, len(lista)):
        if lista[i] != lista[j]:
            novo.append(lista[j])
            i = j

    return novo


print(remover_duplicadas([1, 1, 2, 2, 3]))
