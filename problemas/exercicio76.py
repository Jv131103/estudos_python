"""
Escreva um programa que gere 100 números aleatórios entre 1 e 1000 e
armazene-os em uma lista.
"""
import random

lista = []


for _ in range(100):
    lista.append(random.randint(1, 1000))


print(lista)
