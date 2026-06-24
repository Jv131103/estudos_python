def produto_dos_elementos(lista):
    prefixo = [1] * len(lista)
    for i in range(1, len(lista)):
        prefixo[i] = prefixo[i - 1] * lista[i - 1]

    sufixo = [1] * len(lista)
    for i in range(len(lista) - 2, -1, -1):
        sufixo[i] = sufixo[i + 1] * lista[i + 1]

    resultado = [prefixo[i] * sufixo[i] for i in range(len(lista))]

    return resultado


print(produto_dos_elementos([1, 2, 3, 4]))
