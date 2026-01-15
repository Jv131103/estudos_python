"""
Faça um programa que:

    Leia um número inteiro

    Verifique se ele é primo usando while

    Use else para indicar que não houve divisor

Use divisão e contador.
"""

num = int(input())

total = 0
cont = 2

while cont <= num:
    if num % cont == 0:
        total += 1

    cont += 1

if not total or total > 1:
    print("Não é primo")
elif total == 1:
    print("É primo")
