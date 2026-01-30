"""
Faça um programa que:

    Receba uma lista de números inteiros

    Use map + lambda para:

        elevar todos os números ao quadrado

    Mostre o resultado final

Exemplo conceitual:

    Entrada: [1, 2, 3, 4]
    Saída:   [1, 4, 9, 16]
"""

lista = [1, 2, 3, 4]

saida = list(map(lambda k: k * k, lista))

print(saida)
