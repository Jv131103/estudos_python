"""
Faça um programa que:

    Leia uma palavra

Inverta a palavra usando swap

Não use [::-1]
"""

palavra = input()

lista = list(palavra)

i = 0
j = len(lista) - 1

while i < j:
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp

    i += 1
    j -= 1

invertido = "".join(lista)
print(invertido)
