def soma_diagonal(matriz):
    # diagonal direita
    principal = 0
    for i in range(len(matriz)):
        principal += matriz[i][i]

    # diagonal esquerda
    secundaria = 0
    for i in range(len(matriz)):
        secundaria += matriz[i][len(matriz) - 1 - i]

    return principal, secundaria


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

principal, secundaria = soma_diagonal(mat)
print(f"principal = {principal}")
print(f"secundaria = {secundaria}")
