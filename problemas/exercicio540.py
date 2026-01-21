"""
Faça um programa que:

    Leia L e C

    Construa uma matriz L x C lendo os valores (inteiros)

    Calcule e mostre:

        a soma de cada linha

        a soma de cada coluna

Dicas:

    Para somar linha: um loop em j

    Para somar coluna: um loop em i

    Cuidado com índices: mat[i][j]
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


def somar_cada_linha(mat):
    soma_linhas = []
    soma = 0
    for valor_linha in mat:
        soma = 0
        for valor_coluna in valor_linha:
            soma += valor_coluna
        soma_linhas.append(soma)

    d = {}

    for idx, valor in enumerate(soma_linhas):
        d[f"soma_linha{idx}"] = valor

    return d


def somar_cada_coluna(mat):
    somas_colunas = [0] * len(mat[0])

    for linha in mat:
        for j in range(len(linha)):
            somas_colunas[j] += linha[j]

    d = {}

    for idx, valor in enumerate(somas_colunas):
        d[f"soma_coluna{idx}"] = valor

    return d


linhas = int(input("LINHAS: "))
colunas = int(input("COLUNAS: "))

mat = gerar_matriz(linhas, colunas)
print(somar_cada_linha(mat))
print(somar_cada_coluna(mat))
