def rotacionar(lista, n):
    n = n % len(lista)  # evita erro se n for maior que o tamanho
    return lista[-n:] + lista[:-n]


print(rotacionar([1, 2, 3, 4, 5], 2))
