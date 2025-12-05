def juntar_em_pares(a, b):
    novo = []

    menor = len(a) if len(a) < len(b) else len(b)

    # Enquanto as duas listas ainda tiverem elementos
    for i in range(menor):
        novo.append((a[i], b[i]))

    return novo


print(juntar_em_pares([1, 2, 3], ['a', 'b', 'c']))
# [(1, 'a'), (2, 'b'), (3, 'c')]
