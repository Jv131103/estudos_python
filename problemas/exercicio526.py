"""
Soma de janela fixa

Faça um programa que:

    Receba uma lista de números inteiros

    Receba um valor k

    Calcule a soma de cada janela consecutiva de tamanho k

Mostre todas as somas
"""


def soma_janela_fixa(lista, k):
    # soma da primeira janela
    soma = 0
    for i in range(k):
        soma += lista[i]

    print(soma)

    # desliza a janela
    for i in range(k, len(lista)):
        soma = soma - lista[i - k] + lista[i]
        print(soma)


lista = [1, 2, 3, 4, 5]
k = 3
soma_janela_fixa(lista, k)
