def dobrar(lista):
    nova = []
    for x in lista:
        nova.append(x * 2)
    return nova


def dobrar_elegante(lista):
    return [valor * 2 for valor in lista]


d1 = list(range(100))
print(dobrar(d1))
print(dobrar_elegante(d1))
