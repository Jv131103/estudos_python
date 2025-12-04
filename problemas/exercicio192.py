def rotacionar(lista, k=1):
    n = len(lista)
    novo = [0] * n
    k = k % n

    for i in range(0, n):
        nova_pos = (i + k) % n
        novo[nova_pos] = lista[i]

    return novo


print(rotacionar([1, 2, 3, 4, 5], 2))
