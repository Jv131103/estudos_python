def inserir1(lista, num):
    novo = []

    ja_inseriu = False
    for valor in lista:
        if num <= valor and not ja_inseriu:
            ja_inseriu = True
            novo.append(num)
        novo.append(valor)

    if not ja_inseriu:
        novo.append(num)

    return novo


def inserir2(lista, num):
    novo = []

    for i, valor in enumerate(lista):
        if num <= valor:
            novo.extend(lista[:i])
            novo.append(num)
            novo.extend(lista[i:])
            return novo

    return lista + [num]


def inserir3(lista, num):
    lista.append(None)  # aumenta o tamanho da lista
    i = len(lista) - 2  # começa do último elemento original

    # move elementos maiores para a direita
    while i >= 0 and lista[i] > num:
        lista[i + 1] = lista[i]
        i -= 1

    # insere o número na posição correta
    lista[i + 1] = num

    return lista


def inserir4(lista, num):
    lista.append(num)
    return sorted(lista)


def inserir5(lista, num):
    menores = []
    maiores = []
    inseriu = False

    for v in lista:
        if not inseriu and num <= v:
            inseriu = True
            maiores.append(v)
        elif inseriu:
            maiores.append(v)
        else:
            menores.append(v)

    if not inseriu:
        return lista + [num]
    return menores + [num] + maiores


def inserir6(lista, num):
    i = 0
    while i < len(lista) and lista[i] < num:
        i += 1
    lista.insert(i, num)  # desloca automaticamente
    return lista


def posicao_binaria_left(a, x):
    e, d = 0, len(a)
    while e < d:
        m = (e + d) // 2
        if a[m] < x:
            e = m + 1
        else:
            d = m
    return e


def inserir7(lista, num):
    i = posicao_binaria_left(lista, num)
    lista.insert(i, num)  # shift em C
    return lista


if __name__ == "__main__":
    teste = [
        [1, 4, 6, 10],
        [1, 2, 3, 4, 5, 6],
        [5, 5, 5, 5, 5, 5],
        [1, 2],
        [6, 7, 8],
        []
    ]

    for t in teste:
        print(inserir1(t.copy(), 5))
        print(inserir2(t.copy(), 5))
        print(inserir3(t.copy(), 5))
        print(inserir4(t.copy(), 5))
        print(inserir5(t.copy(), 5))
        print(inserir6(t.copy(), 5))
        print(inserir7(t.copy(), 5))
