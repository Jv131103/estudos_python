def mostrar_somas(lista, k):
    for i in range(len(lista) - k + 1):
        janela = lista[i:i + k]

        soma = 0

        for valor in janela:
            soma += valor

        print(janela, "=", soma)


lista = [4, 2, 7, 1, 8]

mostrar_somas(lista, 3)
