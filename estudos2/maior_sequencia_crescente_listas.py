def maior_sequencia_crescente(lista):
    if not lista:
        return 0

    i = 0
    cont = 1
    maior = 1
    while i + 1 < len(lista):
        if lista[i] < lista[i + 1]:
            cont += 1
        else:
            if cont > maior:
                maior = cont
            cont = 1

        i += 1

    if cont > maior:
        maior = cont

    return maior


print(maior_sequencia_crescente([1, 2, 3, 1, 2, 5, 4]))
print(maior_sequencia_crescente([5, 4, 3, 2]))
print(maior_sequencia_crescente([1, 2, 2, 3, 4]))
print(maior_sequencia_crescente([]))
print(maior_sequencia_crescente([5]))
