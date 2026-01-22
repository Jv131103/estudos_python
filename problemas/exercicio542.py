"""
Faça um programa que:

    Leia um inteiro N

    Leia uma matriz quadrada N x N

    Faça o swap entre os elementos da diagonal principal e da diagonal secundária

    A troca deve ser feita in place

    Mostre a matriz final

Exemplo conceitual:

    Antes:
    1 2 3
    4 5 6
    7 8 9

    Depois:
    3 2 1
    4 5 6
    9 8 7

DICAS:

    Diagonal principal: mat[i][i]

    Diagonal secundária: mat[i][N-1-i]

    Um único loop resolve
"""


def troca_diagonais(mat):
    n = len(mat)

    for diagonal in range(n):
        mat[diagonal][diagonal], mat[diagonal][n - 1 - diagonal] = (
            mat[diagonal][n - 1 - diagonal], mat[diagonal][diagonal]
        )

    return mat


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(troca_diagonais(mat))
