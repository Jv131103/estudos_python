"""
Faça um programa que:

    Crie funções simples: soma, subtração, multiplicação

    Use um dicionário como tabela de decisão para escolher a função

    Leia uma operação e dois números

    Execute a função correta sem usar if/elif

Exemplo conceitual:

    "somar" → função soma
"""


def soma(n1, n2):
    return n1 + n2


def subtracao(n1, n2):
    return n1 - n2


def multiplicacao(n1, n2):
    return n1 * n2


opcoes = {
    "soma": soma,
    "subtracao": subtracao,
    "multiplicacao": multiplicacao
}

print(opcoes["soma"](2, 2))
print(opcoes["subtracao"](2, 1))
print(opcoes["multiplicacao"](2, 3))
