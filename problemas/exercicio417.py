"""
Faça um programa que:

    Peça dois números

    Calcule a média

    Mostre o resultado com 2 casas decimais

Exemplo:

    A média é: 7.50
"""

n1 = float(input("N1: "))
n2 = float(input("N2: "))

media = (n1 + n2) / 2

print(f"A média é: {media:.2f}")
