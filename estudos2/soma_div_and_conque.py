def soma_div_conquer(lista):
    if not lista:
        return 0

    if len(lista) == 1:
        return lista[0]

    meio = len(lista) // 2

    som_esq = lista[:meio]
    soma_dir = lista[meio:]

    return soma_div_conquer(som_esq) + soma_div_conquer(soma_dir)


print(soma_div_conquer([1, 2, 3, 4, 5]))
