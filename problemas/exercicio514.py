"""
Faça um programa que:

    Leia um valor

    Verifique se ele está na lista usando in

    Mostre "Encontrado" ou "Não encontrado"

Objetivo: pertencimento (in).
"""


def busca1(lista, item):
    for valor in lista:
        if valor == item:
            print("Encontrado!")
            return True
    print("Não encontrado!")
    return False


def busca2(lista, item):
    if item in lista:
        print("Encontrado!")
        return True

    print("Não encontrado!")
    return False


def busca3(lista, item):
    lista = sorted(lista)
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == item:
            print("Encontrado!")
            return True
        elif lista[meio] < item:
            inicio = meio + 1
        else:
            fim = meio - 1

    print("Não encontrado!")
    return False


lista = ['a', 'b', 'c']

item = input("Digite um valor qualquer: ")
busca1(lista, item)
busca2(lista, item)
busca3(lista, item)
