from aleatoriedadeMersenneTwister import MT19937


def shuffle_inplace(lista, seed=42):
    if not lista:
        return None

    n = len(lista)

    definicao = MT19937(seed)

    for i in range(n - 1, 0, -1):
        j = definicao.randrange(i + 1)  # [0, i+1)
        lista[i], lista[j] = lista[j], lista[i]

    return lista


def shuffle_newlist(lista, seed=42):
    if not lista:
        return []

    rng = MT19937(seed)

    disponiveis = lista[:]   # cópia da lista original
    resultado = []

    while disponiveis:
        j = rng.randrange(len(disponiveis))   # índice válido
        resultado.append(disponiveis.pop(j))  # remove e adiciona

    return resultado


seed = 42
lista_ordenada = [1, 2, 3, 4, 5, 6]

while seed >= 0:
    print(shuffle_inplace(lista_ordenada.copy(), seed=seed))
    print(shuffle_newlist(lista_ordenada.copy(), seed=seed))
    seed -= 1
