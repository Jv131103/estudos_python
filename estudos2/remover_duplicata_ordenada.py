def remover_duplicata(lista):
    if not lista:  # Tratamento caso a lista venha vazia
        print([])
        return

    lista.sort()  # Garante que as duplicatas fiquem juntas

    left = 0

    for right in range(1, len(lista)):
        if lista[left] != lista[right]:
            left += 1
            lista[left] = lista[right]

    print(lista[:left + 1])


remover_duplicata([1, 1, 2])
remover_duplicata([0, 1, 2, 3, 4, 2, 2, 3, 3, 4])
