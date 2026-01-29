"""
Faça um programa que:

    Tenha uma lista de nomes

    Escolha um nome aleatório usando random.choice

    Repita a escolha algumas vezes
"""
import random

nomes = ["João", "Maria", "Renato", "Matilde", "Dunkan"]


def trazer_nomes_aleatorios_choice(lista):
    return random.choice(lista)


def trazer_nomes_aleatorios_sample(lista, qtd_nomes=1):
    return random.sample(lista, qtd_nomes)


cont = 0
while cont <= 2:
    print(trazer_nomes_aleatorios_choice(nomes))
    print(trazer_nomes_aleatorios_sample(nomes))
    cont += 1
