def lista_eh_estritamente_crescente(lista):
    anterior = lista[0]
    for i in range(1, len(lista)):
        valor = lista[i]
        if valor <= anterior:
            return False
        anterior = valor
    return True


def lista_eh_estritamente_crescente1(lista):
    return all(a < b for a, b in zip(lista, lista[1:]))


print(lista_eh_estritamente_crescente([1, 3, 5, 7]))
print(lista_eh_estritamente_crescente([1, 3, 3, 5]))
print()
print(lista_eh_estritamente_crescente1([1, 3, 5, 7]))
print(lista_eh_estritamente_crescente1([1, 3, 3, 5]))
