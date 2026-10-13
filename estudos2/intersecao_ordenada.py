def intersecao_ordenada(lista1, lista2):
    i = 0
    j = 0
    resultado = []

    while i < len(lista1) and j < len(lista2):
        if lista1[i] == lista2[j]:
            if not resultado or resultado[-1] != lista1[i]:
                resultado.append(lista1[i])
            i += 1
            j += 1
        elif lista1[i] < lista2[j]:
            i += 1
        else:
            j += 1

    return resultado


print(intersecao_ordenada([1, 3, 5, 7, 9, 10], [2, 3, 6, 7, 10]))
print(intersecao_ordenada([], [3, 4, 5]))
print(intersecao_ordenada([1, 2], [3, 4]))
print(intersecao_ordenada([1, 2, 2, 2, 5], [2, 2, 3, 5]))
