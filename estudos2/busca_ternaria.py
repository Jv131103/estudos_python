def busca_ternaria(arr, alvo):

    esquerda = 0
    direita = len(arr) - 1

    while esquerda <= direita:

        terco = (direita - esquerda) // 3

        m1 = esquerda + terco
        m2 = direita - terco

        if arr[m1] == alvo:
            return m1

        if arr[m2] == alvo:
            return m2

        if alvo < arr[m1]:
            direita = m1 - 1

        elif alvo > arr[m2]:
            esquerda = m2 + 1

        else:
            esquerda = m1 + 1
            direita = m2 - 1


lista = range(100)
print(busca_ternaria(lista, 0))
print(busca_ternaria(lista, 25))
print(busca_ternaria(lista, 50))
print(busca_ternaria(lista, 55))
print(busca_ternaria(lista, 99))
