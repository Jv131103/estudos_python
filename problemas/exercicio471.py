"""
Faça um programa que:

    Leia um número inteiro

Verifique se ele é:

    positivo

    negativo

    zero

Mostre o resultado

Use if / elif / else.
"""

num = int(input())

if num == 0:
    print("Zero")
elif num > 0:
    print("Positivo")
else:
    print("Negativo")
