def soma_lista_recursao(lista):
    if not lista:
        return 0

    primeiro = lista[0]
    resto = lista[1:]

    if isinstance(primeiro, list):
        return soma_lista_recursao(primeiro) + soma_lista_recursao(resto)
    else:
        return primeiro + soma_lista_recursao(resto)


print(soma_lista_recursao([1, [2, [3, 4]], 5]))
