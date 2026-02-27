def remover_pares_inplace(lista):
    i = 0

    while i < len(lista):
        if lista[i] % 2 == 0:
            del lista[i]
        else:
            i += 1

    return lista


def remover_pares_inplace2(lista):
    i = 0
    j = len(lista)

    while i < j:
        if lista[i] % 2 == 0:
            lista.pop(i)
            j -= 1
        else:
            i += 1

    return lista


def remover_pares_inplace3(lista):
    pares = []

    filtro = lista[:]

    for valores in filtro:
        if valores % 2 == 0:
            pares.append(valores)

    i = 0
    while i < len(lista):
        if lista[i] in pares:
            lista.pop(i)
        else:
            i += 1

    return lista


def remover_pares_inplace_compact(lista):
    write = 0  # onde vou escrever o próximo ímpar

    for read in range(len(lista)):
        if lista[read] % 2 != 0:
            lista[write] = lista[read]
            write += 1

    # corta o “resto” que sobrou
    del lista[write:]

    return lista


def remover_pares_nao_inplace1(lista):
    return list(filter(lambda i: i % 2 != 0, lista))


def remover_pares_naoinplace_compact(lista):
    return [x for x in lista if x % 2 != 0]


def remover_pares_nao_inplace2(lista):
    novo = []

    for valores in lista:
        if valores % 2 != 0:
            novo.append(valores)

    return novo


def remover_pares_nao_inplace3(lista):
    esquerda = []
    direita = []

    i = 0
    j = len(lista) - 1

    while i <= j:
        if i == j:
            if lista[i] % 2 != 0:
                esquerda.append(lista[i])
        else:
            if lista[i] % 2 != 0:
                esquerda.append(lista[i])

            if lista[j] % 2 != 0:
                direita.append(lista[j])

        i += 1
        j -= 1

    return esquerda + direita[::-1]


print(remover_pares_inplace([2, 3, 4, 5, 6]))
print(remover_pares_inplace([3, 3, 4, 4, 5, 5, 6]))
print(remover_pares_inplace([1, 1, 1, 1]))
print(remover_pares_inplace([2, 4, 6, 8, 10]))
print()
print(remover_pares_inplace_compact([2, 3, 4, 5, 6]))
print(remover_pares_inplace_compact([3, 3, 4, 4, 5, 5, 6]))
print(remover_pares_inplace_compact([1, 1, 1, 1]))
print(remover_pares_inplace_compact([2, 4, 6, 8, 10]))
print()
print(remover_pares_inplace2([2, 3, 4, 5, 6]))
print(remover_pares_inplace2([3, 3, 4, 4, 5, 5, 6]))
print(remover_pares_inplace2([1, 1, 1, 1]))
print(remover_pares_inplace2([2, 4, 6, 8, 10]))
print()
print(remover_pares_inplace3([2, 3, 4, 5, 6]))
print(remover_pares_inplace3([3, 3, 4, 4, 5, 5, 6]))
print(remover_pares_inplace3([1, 1, 1, 1]))
print(remover_pares_inplace3([2, 4, 6, 8, 10]))
print()
print(remover_pares_nao_inplace1([2, 3, 4, 5, 6]))
print(remover_pares_nao_inplace1([3, 3, 4, 4, 5, 5, 6]))
print(remover_pares_nao_inplace1([1, 1, 1, 1]))
print(remover_pares_nao_inplace1([2, 4, 6, 8, 10]))
print()
print(remover_pares_naoinplace_compact([2, 3, 4, 5, 6]))
print(remover_pares_naoinplace_compact([3, 3, 4, 4, 5, 5, 6]))
print(remover_pares_naoinplace_compact([1, 1, 1, 1]))
print(remover_pares_naoinplace_compact([2, 4, 6, 8, 10]))
print()
print(remover_pares_nao_inplace2([2, 3, 4, 5, 6]))
print(remover_pares_nao_inplace2([3, 3, 4, 4, 5, 5, 6]))
print(remover_pares_nao_inplace2([1, 1, 1, 1]))
print(remover_pares_nao_inplace2([2, 4, 6, 8, 10]))
print()
print(remover_pares_nao_inplace3([2, 3, 4, 5, 6]))
print(remover_pares_nao_inplace3([3, 3, 4, 4, 5, 5, 6]))
print(remover_pares_nao_inplace3([1, 1, 1, 1]))
print(remover_pares_nao_inplace3([2, 4, 6, 8, 10]))
