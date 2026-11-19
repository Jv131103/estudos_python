def busca_binaria(numeros, alvo):
    esquerda = 0
    direita = len(numeros) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if numeros[meio] == alvo:
            return meio

        elif numeros[meio] < alvo:
            esquerda = meio + 1

        else:
            direita = meio - 1

    return None


print(busca_binaria([2, 5, 8, 12, 17, 23, 31], 23))
print(busca_binaria([2, 5, 8, 12, 17, 23, 31], 2))
print(busca_binaria([2, 5, 8, 12, 17, 23, 31], 31))
print(busca_binaria([4], 4))
print(busca_binaria([1, 3, 5, 7], 6))
print(busca_binaria([], 10))
print(busca_binaria([1, 3, 5, 7], 7))
