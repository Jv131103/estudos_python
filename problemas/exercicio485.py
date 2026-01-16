"""
Faça um programa que:

    Leia uma lista de números

    Conte quantos são pares

    Use for + if
"""

cont_pares = 0

lista = list(range(0, 10))

pares = []

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
        cont_pares += 1

print(f"Total de pares: {cont_pares}")
print(f"Lista pares: {pares}")
