"""
Faça um programa que:

    . Leia uma palavra

    . Leia outra palavra

    . Compare ignorando maiúsculas/minúsculas

    . Mostre se a primeira vem antes, depois ou é igual à segunda

Dica: use .lower() antes de comparar.
"""
p1 = input("Palavra 1: ").lower()
p2 = input("Palavra 2: ").lower()

if p1 == p2:
    print("iguais")
elif p1 < p2:
    print("P1 vem antes de P2")
else:
    print("P1 vem depois de P2")
