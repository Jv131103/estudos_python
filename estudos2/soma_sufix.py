def soma_suffix(lista):
    if not lista:
        return lista

    suffix = [0] * len(lista)
    suffix[-1] = lista[-1]

    for i in range(len(lista) - 2, -1, -1):
        suffix[i] = suffix[i + 1] + lista[i]

    return suffix


print(soma_suffix([4, 7, 2, 9, 5]))
print(soma_suffix([10, 20, 30, 40]))
