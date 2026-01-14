"""
Faça um programa que:

    Leia uma lista de 5 números (um por vez)

    Verifique se o número 10 está na lista

Mostre o resultado
"""

lista = []

for i in range(5):
    lista.append(int(input()))

print(10 in lista)
