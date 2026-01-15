"""
Faça um programa que:

    Tenha uma lista fixa de números

    Leia um valor do usuário

    Use while para procurar o valor

    Se encontrar, interrompa com break

    Se não encontrar, informe ao final

Use índice manual.
"""

lista_gerada_manualmente = [0, 2, 4, 6, 8, 10]

i = 0

while i < len(lista_gerada_manualmente):
    val = int(input("Digite um número para verificar se existe na lista: "))
    j = 0
    encontrou = False

    while j < len(lista_gerada_manualmente):
        if lista_gerada_manualmente[j] == val:
            encontrou = True
            break

        j += 1

    if encontrou:
        print("Encontrado, parando o laço")
        break

    i += 1
else:
    print("Nenhum valor digitado foi encontrado!")
