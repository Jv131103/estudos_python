"""
Faça um programa que:

    . Leia duas palavras

Mostre:

    . se são iguais

    . se são diferentes
"""

p1 = input("Palavra 1: ")
p2 = input("Palavra 2: ")

iguais = p1 == p2
diferente = p1 != p2

print(f"p1 == p2? {iguais}")
print(f"p1 != p2? {diferente}")
