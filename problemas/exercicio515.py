"""
Faça um programa que:

    Leia uma lista de números

    Leia um valor

    Conte quantas vezes o valor aparece usando count()

Objetivo: método básico de lista.
"""
from random import randint

lista = []

limite = randint(10, 20)
for _ in range(limite):
    lista.append(randint(0, 1000))


print(lista)

num = int(input("Digite um número: "))
total = lista.count(num)

print(f"{num} aparece {total} vezes!")
