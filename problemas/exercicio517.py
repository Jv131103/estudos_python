"""
Faça um programa que:

    Leia uma lista de números

    Encontre o maior e o menor valor

    Sem usar min() nem max()

Objetivo: comparação e controle.
"""
from random import randint

lista = []

limite = randint(5, 20)
for _ in range(limite):
    lista.append(randint(0, 1000))


maior = lista[0]
menor = lista[0]

for valor in lista:
    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

print(f"Lista original: {lista}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
