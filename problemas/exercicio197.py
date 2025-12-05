def mesclar_ordenadas(a, b):
    i = 0
    j = 0
    resultado = []

    # Enquanto as duas listas ainda tiverem elementos
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1

    # Se sobrou coisa em 'a', coloca no final
    while i < len(a):
        resultado.append(a[i])
        i += 1

    # Se sobrou coisa em 'b', coloca no final
    while j < len(b):
        resultado.append(b[j])
        j += 1

    return resultado


print(mesclar_ordenadas([1, 3, 5, 10], [2, 4, 6, 8, 9]))
# [1, 2, 3, 4, 5, 6, 8, 9, 10]
