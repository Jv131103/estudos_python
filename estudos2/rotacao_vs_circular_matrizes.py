def get_circular(mat, i, j):
    n = len(mat)
    return mat[i % n][j % n]


def rotacionar_90(mat):
    n = len(mat)
    nova = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            nova[j][n - 1 - i] = mat[i][j]

    return nova


mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(get_circular(mat, 3, 0))   # 1
print(get_circular(mat, -1, 1))  # 8

print(rotacionar_90(mat))
