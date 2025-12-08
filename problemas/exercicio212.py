def maior(lista):
    if len(lista) == 1:
        return lista[0]

    maior_do_resto = maior(lista[1:])

    if lista[0] > maior_do_resto:
        return lista[0]
    else:
        return maior_do_resto


print(maior([10, 4, 2, 88, 3, 15]))  # 88
