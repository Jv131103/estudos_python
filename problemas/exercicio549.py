"""
Faça um programa que:

    Leia uma lista de palavras

    Crie um dicionário que conte quantas vezes cada palavra aparece

    Mostre o dicionário final

Exemplo conceitual:

    ["a", "b", "a", "c", "b", "a"]
    → {"a":3, "b":2, "c":1}
"""


def retornar_contagem(lista):
    d = {}

    for valor in lista:
        d[valor] = d.get(valor, 0) + 1

    return d


lista = ["a", "b", "a", "c", "b", "a"]
dados = retornar_contagem(lista)
print(dados)
