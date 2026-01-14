"""
Faça um programa que:

    Leia dois números

    Faça o swap usando variável auxiliar

    Mostre os valores antes e depois da troca
"""

a = int(input())
b = int(input())
print(f"{a=}, {b=}")

temp = a
a = b
b = temp
print(f"{a=}, {b=}")
