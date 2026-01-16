"""
Crie uma função filtrar_pares(lista) usando lambda + filter para retornar
apenas os números pares de uma lista.
"""


def filtrar_pares(lista):
    return list(filter(lambda v: v % 2 == 0, lista))


print(filtrar_pares([1, 2, 3, 4, 5, 6]))
