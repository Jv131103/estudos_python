"""
Faça um programa que:

    Peça dois números

Calcule:

    soma

    subtração

    multiplicação

Mostre os resultados
"""

n1 = float(input("N1: "))
n2 = float(input("N2: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2

print(f"{n1} + {n2} = {soma}")
print(f"{n1} - {n2} = {subtracao}")
print(f"{n1} x {n2} = {multiplicacao}")
