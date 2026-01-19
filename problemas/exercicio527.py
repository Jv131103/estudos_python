"""
Faça um programa que:

    Receba uma lista de números

    Receba um valor k

    Encontre a maior soma entre todas as janelas consecutivas de tamanho k

Use janela deslizante (não força bruta).
"""


def soma_maior_janela(lista, k):
    # soma da primeira janela
    soma = 0
    for i in range(k):
        soma += lista[i]

    maior = soma

    # desliza a janela
    for i in range(k, len(lista)):
        soma = soma - lista[i - k] + lista[i]
        if soma > maior:
            maior = soma

    return maior


lista = [1, 2, 3, 4, 5]
k = 3
print(soma_maior_janela(lista, k))
