def sliding_basico(lista, k):
    soma = 0

    # soma apenas a primeira janela
    for i in range(k):
        soma += lista[i]

    print("Primeira janela:", soma)

    for i in range(k, len(lista)):
        saiu = lista[i - k]
        entrou = lista[i]

        soma = soma - saiu + entrou

        print("Saiu:", saiu)
        print("Entrou:", entrou)
        print("Nova soma:", soma)
        print()


lista = [4, 2, 7, 1, 8]
sliding_basico(lista, 3)
