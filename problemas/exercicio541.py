"""
Faça um programa que:

    Leia L e C

    Leia uma matriz L x C

    Crie a matriz transposta C x L (sem usar libs)

    Imprima a transposta formatada

Dicas:

    Na transposta: T[j][i] = A[i][j]

    Você pode criar T com loops e append
"""


def gerar_matriz(linhas, colunas):
    mat = []
    for i in range(linhas):
        lin = []
        for j in range(colunas):
            valor = int(input(f"VALOR [{i}][{j}]: "))
            lin.append(valor)
        mat.append(lin)

    return mat


def criar_transposta(mat):
    transposta = []

    for linha in range(len(mat[0])):
        new = []
        for coluna in range(len(mat)):
            new.append(mat[coluna][linha])
        transposta.append(new)

    return transposta


linhas = int(input("LINHAS: "))
colunas = int(input("COLUNAS: "))
print(criar_transposta(gerar_matriz(linhas, colunas)))
