def soma_prefix(lista):
    if not lista:
        return lista

    prefix = [0] * len(lista)
    prefix[0] = lista[0]

    for i in range(1, len(lista)):
        prefix[i] = prefix[i - 1] + lista[i]

    return prefix


print(soma_prefix([4, 7, 2, 9, 5]))
print(soma_prefix([10, 20, 30, 40]))
