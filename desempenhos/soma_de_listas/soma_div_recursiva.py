def soma_div_conquer(lista):
    if not lista:
        return 0

    if len(lista) == 1:
        return lista[0]

    meio = len(lista) // 2

    som_esq = lista[:meio]
    soma_dir = lista[meio:]

    return soma_div_conquer(som_esq) + soma_div_conquer(soma_dir)


def soma_recursiva(lista):
    if not lista:
        return 0

    if len(lista) == 1:
        return lista[0]

    return lista[0] + soma_recursiva(lista[1:])


def soma_recursiva2(lista, i=0):
    if not lista or i >= len(lista):
        return 0

    return lista[i] + soma_recursiva2(lista, i=i + 1)
