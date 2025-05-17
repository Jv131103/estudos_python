"""
Faça um programa, com uma função, que calcula a mediana de uma lista.

Funções embutidas podem ajudar:

    . sorted(lista): ordena a lista
"""


def mediana(lista):
    lista = sorted(lista)
    if len(lista) % 2 != 0:
        return lista[len(lista) // 2]
    else:
        meio = (lista[len(lista) // 2 - 1] + lista[len(lista) // 2]) / 2
        return meio


if __name__ == "__main__":
    print(mediana([1, 2, 3, 4, 5]))
    print(mediana([2, 3, 4, 5]))
