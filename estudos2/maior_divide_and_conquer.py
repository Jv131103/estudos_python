def maior_div_conquista(lista):
    if len(lista) == 1:
        return lista[0]

    meio = len(lista) // 2

    maior_esq = maior_div_conquista(lista[:meio])
    maior_dir = maior_div_conquista(lista[meio:])

    if maior_esq > maior_dir:
        return maior_esq
    else:
        return maior_dir


print(maior_div_conquista([2, 7, 1, 9, 4]))
