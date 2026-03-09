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


if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(espiral(matriz))
