"""
Faça um programa que:

    Leia um número inteiro positivo

    Faça uma contagem regressiva até 0

Mostre cada valor

Dica: use decremento (-=).
"""

n = int(input())
print("Realizando decremento...")

while n >= 0:
    print(n)
    n -= 1
