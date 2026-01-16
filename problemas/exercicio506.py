"""
Faça uma função recursiva que:

    Receba uma lista que pode conter listas

    Retorne a soma de todos os números

Exemplo:

    [1, [2, [3, 4]], 5]


Resultado:

    15


Dica: teste tipo com isinstance.
"""


def soma_lista_for(lista):
    soma = 0

    for elemento in lista:
        if isinstance(elemento, list):
            soma += soma_lista_for(elemento)  # recursão
        else:
            soma += elemento              # caso base

    return soma


def soma_lista_recursao(lista):
    if not lista:
        return 0

    primeiro = lista[0]
    resto = lista[1:]

    if isinstance(primeiro, list):
        return soma_lista_recursao(primeiro) + soma_lista_recursao(resto)
    else:
        return primeiro + soma_lista_recursao(resto)


print(soma_lista_recursao([1, [2, [3, 4]], 5]))
