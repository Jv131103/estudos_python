"""
Faça um programa que:

    Receba uma lista de números

    Substitua in place:

        a primeira metade da lista por zeros

    A segunda metade deve permanecer intacta

    Use slicing com atribuição

Não crie uma nova lista para o resultado final
"""
lista = [1, 2, 4, 5, 6]

metade = len(lista) // 2

lista[:metade] = [0] * metade
print(lista)
