def espiral(m):
    resultado = []

    top = 0
    bottom = len(m) - 1
    left = 0
    right = len(m[0]) - 1

    while top <= bottom and left <= right:

        for j in range(left, right + 1):
            resultado.append(m[top][j])
        top += 1

        for i in range(top, bottom + 1):
            resultado.append(m[i][right])
        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                resultado.append(m[bottom][j])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                resultado.append(m[i][left])
            left += 1

    return resultado


def espiral_direcoes(m):

    linhas = len(m)
    colunas = len(m[0])

    visitado = [[False] * colunas for _ in range(linhas)]

    direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    d = 0
    i = j = 0

    resultado = []

    for _ in range(linhas * colunas):

        resultado.append(m[i][j])
        visitado[i][j] = True

        ni = i + direcoes[d][0]
        nj = j + direcoes[d][1]

        if (
            0 <= ni < linhas
            and 0 <= nj < colunas
            and not visitado[ni][nj]
        ):
            i, j = ni, nj
        else:
            d = (d + 1) % 4
            i += direcoes[d][0]
            j += direcoes[d][1]

    return resultado


def espiral_pop(m):

    resultado = []

    while m:

        resultado += m.pop(0)

        if m and m[0]:
            for linha in m:
                resultado.append(linha.pop())

        if m:
            resultado += m.pop()[::-1]

        if m and m[0]:
            for linha in reversed(m):
                resultado.append(linha.pop(0))

    return resultado


if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(espiral(matriz))
    print(espiral_direcoes(matriz))
    print(espiral_pop(matriz))
