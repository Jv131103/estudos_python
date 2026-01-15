"""
Leia uma lista de números.

    Verifique se a lista não está vazia

    Verifique se o número 10 está presente

    Só imprima "OK" se ambas as condições forem verdadeiras

Use and e in.
"""


def validar(lista):
    if lista and 10 in lista:
        print("Ok")
        return
    print("Não Ok")


listas = [
    [2, 4, 6, 8, 10],
    [],
    [2, 4, 6, 8],
    [10]
]

for lista in listas:
    validar(lista)
