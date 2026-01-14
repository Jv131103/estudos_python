"""
Faça um programa que:

    Leia um número decimal como texto

    Converta para float

Mostre o valor arredondado com 2 casas
"""
num = input().replace(",", ".")
num = float(num)

print(f"{num:.2f}")
