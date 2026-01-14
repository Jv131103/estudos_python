"""
Faça um programa que:

    Leia dois nomes

    Diga qual vem primeiro em ordem alfabética

Use operadores relacionais.
"""

nome1 = input("Nome1: ").lower()
nome2 = input("Nome2: ").lower()

if nome1 == nome2:
    print("Os nomes são iguais")
elif nome1 < nome2:
    print("Nome 1 vem primeiro")
else:
    print("Nome 2 vem primeiro")
