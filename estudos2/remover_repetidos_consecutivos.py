def remover_repetidos_consecutivos(lista):
    if not lista:
        return []

    i = 1
    novo = [lista[0]]

    while i < len(lista):
        if lista[i] != novo[-1]:
            novo.append(lista[i])

        i += 1

    return novo


print(remover_repetidos_consecutivos([1, 1, 1, 2, 2, 3, 1, 1, 4, 4]))
print(remover_repetidos_consecutivos([1, 1, 2, 3]))
print(remover_repetidos_consecutivos([7]))
print(remover_repetidos_consecutivos([]))
