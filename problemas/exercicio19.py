"""
Faça um programa, com uma função, que calcula a dispersão de uma lista

    Funções embutidas que podem te ajudar:

        . min(lista) -> retorna o menor valor da lista

        . max(lista) -> retorna o maior valor da lista

"""


def dispersao(*lista):
    return max(lista) - min(lista)


print(dispersao(1, 2, 3, 4))
