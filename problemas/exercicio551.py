"""
Faça um programa que:

    Dado um dicionário simples:

        nome → idade

    Crie um novo dicionário invertido:

        idade → nome

    Mostre o resultado
"""


dados = {"João": 22}

inverso = {}
for chave, valor in dados.items():
    inverso[valor] = chave

print(inverso)
