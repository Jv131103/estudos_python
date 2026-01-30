"""
Curto-circuito funcional

Faça um programa que:

    Receba uma lista de números

Verifique:

    se existe pelo menos um número negativo (any)

    se todos os números são pares (all)

    Use expressões geradoras, não listas
"""


def tratar_erros(lista):
    if not isinstance(lista, list):
        raise TypeError("PARÂMETRO LISTA, PRECISA DO TIPO LIST")

    if not lista:
        raise ValueError("LISTA NÃO PODE ESTAR VAZIA")


def verificacao(lista):
    tratar_erros(lista)

    any_negativo = any(x < 0 for x in lista)
    all_pares = all(x % 2 == 0 for x in lista)

    print(f"any negativo → {any_negativo}")
    print(f"all pares → {all_pares}")


verificacao([2, 4, 6, -1])
