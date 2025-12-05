def intercalar(a, b):
    novo = []

    tamanho = min(len(a), len(b))

    for i in range(tamanho):
        novo.append(a[i])
        novo.append(b[i])

    # Se uma lista for maior, adiciona o restante
    for i in range(tamanho, len(a)):
        novo.append(a[i])
    for i in range(tamanho, len(b)):
        novo.append(b[i])

    return novo


print(intercalar([1, 2, 3], ['a', 'b', 'c']))
# [1, 'a', 2, 'b', 3, 'c']

print(intercalar([1, 2, 3], ['a', 'b', 'c', 'd']))
# [1, 'a', 2, 'b', 3, 'c', 'd']

print(intercalar([1, 2, 3, 4], ['a', 'b', 'c']))
# [1, 'a', 2, 'b', 3, 'c', 4]
