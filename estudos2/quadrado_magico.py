def eh_quadrado_magico(mat):
    n = len(mat)
    if n == 0:
        return False

    # soma alvo: primeira linha
    alvo = 0
    for j in range(n):
        alvo += mat[0][j]

    # somas das linhas
    for i in range(n):
        soma_linha = 0
        for j in range(n):
            soma_linha += mat[i][j]
        if soma_linha != alvo:
            return False

    # somas das colunas
    for j in range(n):
        soma_coluna = 0
        for i in range(n):
            soma_coluna += mat[i][j]
        if soma_coluna != alvo:
            return False

    # diagonal principal
    soma_diag1 = 0
    for i in range(n):
        soma_diag1 += mat[i][i]
    if soma_diag1 != alvo:
        return False

    # diagonal secundária
    soma_diag2 = 0
    for i in range(n):
        soma_diag2 += mat[i][n - 1 - i]
    if soma_diag2 != alvo:
        return False

    return True


# Leitura (exemplo padrão)
n = int(input())
mat = []
for _ in range(n):
    linha = list(map(int, input().split()))
    mat.append(linha)

print("SIM" if eh_quadrado_magico(mat) else "NAO")
