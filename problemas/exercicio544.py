"""
Swap entre diagonal principal e uma coluna

Faça um programa que:

    Leia um inteiro N

    Leia uma matriz quadrada N x N

    Leia um índice de coluna c

    Faça o swap entre os elementos da diagonal principal e os elementos da coluna c

    A operação deve ser feita in place

    Mostre a matriz final

Exemplo conceitual:

    Diagonal principal ↔ Coluna c
    mat[i][i] ↔ mat[i][c]

DICAS

    Use um único loop em i

    Garanta que c está no intervalo válido

    Pense no impacto visual dessa troca

Objetivo:

    treinar swap estrutural não simétrico, muito comum em algoritmos reais.
"""


def troca(mat, coluna):
    n = len(mat)

    if coluna < 0 or coluna >= n:
        raise ValueError("Índice de coluna inválido")

    for diagonal in range(n):
        mat[diagonal][diagonal], mat[diagonal][coluna] = mat[diagonal][coluna], mat[diagonal][diagonal]

    return mat


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(troca(mat, 1))
