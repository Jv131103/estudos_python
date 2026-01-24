"""
Faça um programa que:

    Leia uma lista de nomes e suas cidades

    Agrupe os nomes por cidade em um dicionário

Exemplo conceitual:

    "Ana" → "SP"
    "João" → "RJ"

Resultado:

    {"SP": ["Ana"], "RJ": ["João"]}
"""

lista = [("Ana", "SP"), ("João", "RJ"), ("Carlinhos", "SP")]


def criar(dados):
    d = {}

    for dado in dados:
        nome, estado = dado

        d.setdefault(estado, []).append(nome)

    return d


print(criar(lista))
