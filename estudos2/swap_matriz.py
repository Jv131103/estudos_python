LINHAS = 3
COLUNAS = 4


def trocar_linhas(matriz, i, j):
    matriz[i], matriz[j] = matriz[j], matriz[i]
    return matriz


def trocar_linha_e_coluna(matriz, linha1, coluna1, linha2, coluna2):
    matriz[linha1][coluna1], matriz[linha2][coluna2] = matriz[linha2][coluna2], matriz[linha1][coluna1]
    return matriz


def gerar_aleatorios(mat, inicio, fim):
    from random import randint

    for i in range(LINHAS):
        for j in range(COLUNAS):
            mat[i][j] = randint(inicio, fim)

    return mat


mat = [[0] * COLUNAS for _ in range(LINHAS)]

novo_mat = gerar_aleatorios(mat, 0, 1000)
print(novo_mat)

print(trocar_linhas(mat, 0, 1))
print(trocar_linha_e_coluna(mat, 0, 2, 1, 2))
