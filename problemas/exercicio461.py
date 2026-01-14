"""
Faça um programa que:

    Leia três números reais

    Calcule a média

Mostre o resultado com 2 casas decimais
"""
n1 = float(input().replace(",", "."))
n2 = float(input().replace(",", "."))
n3 = float(input().replace(",", "."))

media = (n1 + n2 + n3) / 3

print(f"Média: {media:.2f}")
