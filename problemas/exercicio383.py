def maior_sequencia(lista):
    anterior = lista[0]

    cont = 1
    maior = cont
    for i in range(1, len(lista)):
        atual = lista[i]
        if atual == anterior:
            cont += 1
        else:
            anterior = atual
            cont = 1

        if cont > maior:
            maior = cont

    return maior


print(maior_sequencia([1, 1, 2, 2, 2, 3, 3, 1]))
