def soma_maiores_que_10(lista):
    soma = 0
    for indice in range(len(lista)):
        if lista[indice] > 10:
            soma += lista[indice]
    return soma


print(soma_maiores_que_10([2, 4, 6, 8, 9, 10, 12]))
