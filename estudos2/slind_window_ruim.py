def window_ruim(lista, key):
    lista_maiores = []

    for i in range(len(lista) - key + 1):
        cont = 0
        maior = lista[i]
        for j in range(i, len(lista)):
            if cont == key:
                break

            if lista[j] > maior:
                maior = lista[j]

            cont += 1

        lista_maiores.append(maior)

    print(lista_maiores)


def window_ruim2(lista, key):
    lista_maiores = []

    for i in range(len(lista) - key + 1):
        tres_itens = lista[i:i + key]
        lista_maiores.append(max(tres_itens))

    print(lista_maiores)


nums = [1, 3, -1, -3, 5, 3, 6, 7]
window_ruim(nums, 3)
window_ruim2(nums, 3)
