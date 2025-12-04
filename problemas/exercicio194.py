def par(numero):
    return numero % 2 == 0


def informacao_lista(listas):
    pares = [numero for numero in listas if par(numero)]

    soma_pares = 0
    for num_par in pares:
        soma_pares += num_par

    print(listas)
    print(pares)
    print(soma_pares)


informacao_lista([3, 8, 2, 9, 10])
