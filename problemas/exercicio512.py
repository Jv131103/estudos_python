"""
Faça um programa que:

    Crie uma lista com 5 números inteiros

    Modifique o primeiro e o último elemento

    Mostre a lista final

Objetivo: índice e mutabilidade.
"""

lista = []

for i in range(5):
    valor = int(input(f"Adicionar no índice {i}: "))
    lista.append(valor)


print(f"Lista original: {lista}")

# Forma de treino de troca
temp = lista[0]
lista[0] = lista[len(lista) - 1]
lista[len(lista) - 1] = temp
print(f"Lista trocada: {lista}")

# Voltando ao normal
lista[0], lista[-1] = lista[-1], lista[0]
print(f"Lista normalizada: {lista}")
