"""
Faça um programa que:

    Leia um número decimal

Verifique se ele é inteiro usando is_integer()

Se for, converta para int
"""

n = float(input())

if n.is_integer():
    n = int(n)

    print(f"Conversão: {n}")
