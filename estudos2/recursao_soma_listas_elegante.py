def soma_recursiva(lista):
    if not lista:        # caso base: lista vazia
        return 0
    return lista[0] + soma_recursiva(lista[1:])


print(soma_recursiva([1, 2, 3, 4]))
