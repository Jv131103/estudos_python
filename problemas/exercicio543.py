"""
Swap de diagonais paralelas à principal

Faça um programa que:

    Leia um inteiro N

    Leia uma matriz quadrada N x N

    Faça o swap entre:

        a diagonal imediatamente acima da principal (j - i = 1)

        a diagonal imediatamente abaixo da principal (j - i = -1)

Modifique a matriz in place

Mostre o resultado

Exemplo visual (X = principal):

    . A .
    B X C
    . D .

Trocar A ↔ B e C ↔ D.

DICAS

    Use a relação j = i + 1 e j = i - 1

    Verifique se os índices são válidos

    Cuidado para não acessar fora da matriz

Objetivo:

    entender que diagonais não são só duas.
"""


def swap_diagonais_paralelas(mat):
    N = len(mat)

    for i in range(1, N - 1):
        # swap: acima ↔ abaixo da principal
        mat[i][i + 1], mat[i][i - 1] = mat[i][i - 1], mat[i][i + 1]

    return mat


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(swap_diagonais_paralelas(mat))
