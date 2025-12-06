def intercalar(lista1, lista2):
    novo = []

    menor = len(lista1) if len(lista1) < len(lista2) else len(lista2)

    # Enquanto as duas listas ainda tiverem elementos
    for i in range(menor):
        novo.append(lista1[i])
        novo.append(lista2[i])

    return novo


A = [1, 3, 5]
B = [2, 4, 6]
print(intercalar(A, B))
