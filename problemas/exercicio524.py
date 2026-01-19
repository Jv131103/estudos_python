"""
Faça um programa que:

    Receba uma lista de números

    Inverta a lista in place

    Não use reverse() nem [::-1]

    Use swap com índices

Regras:

    Use dois índices (i e j)

    Não crie lista auxiliar

"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
j = len(lista) - 1

while i <= j:
    lista[i], lista[j] = lista[j], lista[i]

    i += 1
    j -= 1

print(lista)
