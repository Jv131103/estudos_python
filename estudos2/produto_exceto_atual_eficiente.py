
def produto_exceto_atual(lista):
    resultado = [1] * len(lista)

    prefixo = 1

    for i in range(len(lista)):
        resultado[i] = prefixo
        prefixo *= lista[i]

    sufixo = 1

    for i in range(len(lista) - 1, -1, -1):
        resultado[i] *= sufixo
        sufixo *= lista[i]

    return resultado


lista = [1, 2, 3, 4]
print(produto_exceto_atual(lista))
