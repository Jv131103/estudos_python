def rotacionar_direita(numeros, passos):
    if not numeros:
        return []

    deslocamento = passos % len(numeros)

    if deslocamento == 0:
        return numeros.copy()

    resultado = (
        numeros[-deslocamento:]
        + numeros[:-deslocamento]
    )

    return resultado


print(rotacionar_direita([10, 20, 30, 40, 50], 2))
print(rotacionar_direita([1, 2, 3, 4], 1))
print(rotacionar_direita([7, 8, 9], 3))
print(rotacionar_direita([1, 2, 3], 5))
print(rotacionar_direita([], 3))
print(rotacionar_direita([1, 2, 3, 4], 0))
print(rotacionar_direita([42], 100))
