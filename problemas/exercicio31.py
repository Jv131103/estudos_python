"""
Escreva um programa que peça um número inteiro do usuário e calcule e imprima a
tabuada deste número.
"""


def tabuada(n, limite=10):
    for i in range(limite + 1):
        print(f"{n} x {i} = {n * i}")
    print()


def iter_tabuada(inicio=0, fim=10, limite=10):
    for i in range(inicio, fim + 1):
        tabuada(i, limite)


iter_tabuada(1, 5)
