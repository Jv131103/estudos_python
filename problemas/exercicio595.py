"""
Faça um programa que:

    Tenha uma lista de números

    Verifique se o tamanho da lista é maior que 5

    Guarde o tamanho em uma variável dentro do if usando walrus

    Imprima o tamanho se a condição for verdadeira
"""

lista = [1, 2, 3, 4, 5]

if (tam := len(lista)) >= 5:
    print("Lista é maior ou igual a 5")
    print(f"Tamanho: {tam}")
