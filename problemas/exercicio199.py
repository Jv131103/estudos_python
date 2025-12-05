def intercalar(a, b):
    i = 0
    j = 0

    novo = []

    # Enquanto as duas listas ainda tiverem elementos
    while i < len(a) and j < len(b):
        novo.append(a[i])
        novo.append(b[j])
        i += 1
        j += 1

    # Se sobrou coisa em 'a', coloca no final
    while i < len(a):
        novo.append(a[i])
        i += 1

    # Se sobrou coisa em 'b', coloca no final
    while j < len(b):
        novo.append(b[j])
        j += 1

    return novo


print(intercalar([1, 2, 3], ['a', 'b', 'c']))
print(intercalar([1, 2, 3], ['a', 'b', 'c', 'd']))
print(intercalar([1, 2, 3, 4], ['a', 'b', 'c']))
