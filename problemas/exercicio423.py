"""
Faça um programa que:

    Leia dois números

Calcule a diferença entre eles

    Mostre a diferença sem sinal

    Mostre o valor arredondado com 2 casas

Use abs() e round().
"""

n1 = float(input())
n2 = float(input())

diferenca = round(abs(n1 - n2), 2)
print(f"Diferença: {diferenca}")
