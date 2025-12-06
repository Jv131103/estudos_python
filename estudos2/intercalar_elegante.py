def intercalar(a, b):
    resultado = []
    for x, y in zip(a, b):
        resultado.extend([x, y])
    return resultado


A = [1, 3, 5]
B = [2, 4, 6]
print(intercalar(A, B))
