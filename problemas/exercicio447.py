"""
Faça um programa que:

    Leia dois números

    Faça o swap usando a forma do Python

Mostre os valores antes e depois
"""

a = int(input())
b = int(input())
print(f"{a=}, {b=}")

a, b = b, a
print(f"{a=}, {b=}")
