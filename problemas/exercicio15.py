"""
Faça um programa que dada a entrada de uma lista o programa calcule a combinatória de
dois elementos e nos retorne as combinações em uma nova lista.

    Exemplo de entrada: [1, 2, 3, 4]

    Exemplo de saída: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

"""

lista = [1, 2, 3, 4]
new = []

for i in range(0, len(lista)):
    for j in range(i + 1, len(lista)):
        new.append([lista[i], lista[j]])

print(new)
