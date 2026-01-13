"""
Faça um programa que:

    . Leia dois números

Mostre:

    . divisão normal (/)

    . divisão inteira (//)

    . resto da divisão (%)

Mostre cada resultado em uma linha.
"""
n1 = float(input("N1: "))
n2 = float(input("N2: "))

if n2 == 0:
    print("Impossível divisão por 0")
else:
    div_normal = n1 / n2
    div_int = n1 // n2
    div_rest = n1 % n2

    print(f"Divisão normal: {div_normal}")
    print(f"Divisão inteira: {div_int}")
    print(f"Resto da divisão: {div_rest}")
