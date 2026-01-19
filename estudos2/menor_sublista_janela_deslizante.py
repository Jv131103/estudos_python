def menor_sublista_soma_ge_x(lista, x):
    left = 0
    soma = 0
    melhor = float("inf")

    for right in range(len(lista)):
        soma += lista[right]  # expande janela (entra)

        while soma >= x:      # encolhe janela (sai) enquanto ainda serve
            tamanho = right - left + 1
            if tamanho < melhor:
                melhor = tamanho

            soma -= lista[left]
            left += 1

    return 0 if melhor == float("inf") else melhor


lista = [2, 3, 1, 2, 4, 3]
x = 7
print(menor_sublista_soma_ge_x(lista, x))  # 2 (sublista [4,3])
