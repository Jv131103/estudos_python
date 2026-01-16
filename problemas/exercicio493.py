"""
Crie uma função media(*valores) que receba uma quantidade variável de números
e retorne a média aritmética.
"""


def versao1(*valores):
    return sum(valores) / len(valores)


def versao2(*valores):
    soma = 0
    qtd = 0

    for valor in valores:
        soma += valor
        qtd += 1

    return soma / qtd


print(versao1(10, 10, 10, 10))
print(versao2(10, 10, 10, 10))
print()
print(versao1(5, 10, 6, 7))
print(versao2(5, 10, 6, 7))
