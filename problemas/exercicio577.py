"""
Faça um programa que:

    Dada uma lista de números

    Crie um gerador de expressão que produza apenas os números pares

    Use o gerador com sum() e list()

    Observe o comportamento após o consumo

Exemplo conceitual:

    Entrada: [1, 2, 3, 4, 5, 6]
    Saída (list): [2, 4, 6]
    Saída (sum): 12
"""


def retornar_especificacoes(lista):
    pares = (x for x in lista if x % 2 == 0)

    lista_pares = list(pares)
    soma_pares = sum(pares)  # gerador já foi consumido

    return {
        "lista_pares": lista_pares,
        "soma": soma_pares
    }


print(retornar_especificacoes([1, 2, 3, 4, 5, 6]))
