def mostrar_janelas(lista, k):
    for i in range(len(lista) - k + 1):
        janela = lista[i:i + k]
        print(janela)


lista = [4, 2, 7, 1, 8]

mostrar_janelas(lista, 3)
