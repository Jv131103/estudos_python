"""
Faça um programa que:

    Receba uma lista de números

    Embaralhe a lista manualmente, seguindo exatamente este processo:

Passos obrigatórios:

    1. Comece do último índice da lista

    2. Gere um índice aleatório entre 0 e o índice atual

    3. Faça swap entre o elemento atual e o elemento aleatório

    4. Vá diminuindo o índice até chegar ao início da lista

Regras:

    Use random.randint

    Use swap in place

    Não use random.shuffle

    Não use sorted

    Não crie uma nova lista

DICAS

    Use um loop que vai de len(lista) - 1 até 1

    Pense: “essa posição já ficou definitiva?”
"""


from random import randint


def shuffle(lista):
    n = len(lista)

    # começa do último índice e vai até 1
    for i in range(n - 1, 0, -1):
        j = randint(0, i)   # índice aleatório entre 0 e i

        # swap in place
        lista[i], lista[j] = lista[j], lista[i]

    return lista


print(shuffle([1, 2, 3, 4, 5]))
print(shuffle([1, 2, 3, 4, 5]))
print(shuffle([1, 2, 3, 4, 5]))
