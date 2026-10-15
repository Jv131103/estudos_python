def achatar_lista(matriz):
    novo = []
    for lista in matriz:
        for valor in lista:
            novo.append(valor)

    return novo


print(achatar_lista([[1, 2], [3, 4], [5]]))
print(achatar_lista([[10], [], [20, 30]]))
print(achatar_lista([]))
print(achatar_lista([[], []]))
