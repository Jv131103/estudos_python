"""
Faça um programa que:

    Receba uma lista de números

    Use filter + lambda para manter apenas:

        números maiores que 10

        Use sum() para somar os valores filtrados

    Mostre o resultado

Exemplo conceitual:

    Entrada: [5, 12, 7, 20, 3, 15]
    Saída:   47   # 12 + 20 + 15
"""


lista = [5, 12, 7, 20, 3, 15]

soma_maiores_que_dez = sum(filter(lambda k: k > 10, lista))

print(soma_maiores_que_dez)
