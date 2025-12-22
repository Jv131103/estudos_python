def repetidos(lista1, lista2):
    l1 = sorted(lista1)
    l2 = sorted(lista2)

    i = j = 0
    resultado = []

    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            if not resultado or resultado[-1] != l1[i]:
                resultado.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1

    return resultado


a = [1, 2, 2, 3, 5]
b = [2, 2, 4, 5, 6]
print(repetidos(a, b))
