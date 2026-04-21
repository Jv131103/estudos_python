import timeit
import random


def busca_index(lista, valor):
    try:
        return lista.index(valor)
    except ValueError:
        return -1


def busca_linear(lista, valor):
    for i, dado in enumerate(lista):
        if dado == valor:
            return i
    return -1


def busca_binaria(lista, valor):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1


# Dados ordenados:
dados_ordenados = {
    10: list(range(10)),
    100: list(range(100)),
    1000: list(range(1000)),
    10000: list(range(10000)),
}

# Dados desordenados:
dados_desordenados = {}
for n in [10, 100, 1000, 10000]:
    lista = list(range(n))
    random.shuffle(lista)
    dados_desordenados[n] = lista


# Buscas:
def gerar_casos(lista):
    n = len(lista)
    return {
        "inicio": lista[0],
        "meio": lista[n // 2],
        "fim": lista[-1],
        "ausente": -1
    }


for n, lista in dados_ordenados.items():
    casos = gerar_casos(lista)

    print(f"\nTamanho: {n}")

    for nome_caso, valor in casos.items():
        for _ in range(100):
            busca_linear(lista, valor)
            busca_index(lista, valor)
            busca_binaria(lista, valor)

        t_linear = min(timeit.repeat(lambda: busca_linear(lista, valor), repeat=5, number=1000))
        t_index = min(timeit.repeat(lambda: busca_index(lista, valor), repeat=5, number=1000))
        t_binaria = min(timeit.repeat(lambda: busca_binaria(lista, valor), repeat=5, number=1000))

        print(f"\nCaso: {nome_caso}")
        print(f"Linear : {t_linear:.8f}")
        print(f"Index  : {t_index:.8f}")
        print(f"Binária: {t_binaria:.8f}")
