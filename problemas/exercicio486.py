"""
Faça um programa que:

    Leia um número

    Procure esse número em uma lista

    Se encontrar, interrompa

    Se não encontrar, use else para avisar

Use break e for else.
"""

num = int(input())

lista_gerada_manualmente = [0, 2, 4, 6, 8, 10]

# Usando esse modelo, afim de estudo
for valor in range(len(lista_gerada_manualmente)):
    if lista_gerada_manualmente[valor] == num:
        print("Valor encontrado")
        break
else:
    print("Valor não encontrado na lista")
