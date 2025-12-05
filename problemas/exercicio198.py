def soma_maxima_subarray(lista):
    if not lista:
        raise ValueError("Lista não pode ser vazia")

    soma_atual = lista[0]
    melhor_soma = lista[0]

    for x in lista[1:]:
        # ou eu continuo somando, ou recomeço em x
        soma_atual = max(x, soma_atual + x)
        # atualizo o melhor que já vi
        melhor_soma = max(melhor_soma, soma_atual)

    return melhor_soma


print(soma_maxima_subarray([1, -3, 2, 1, -1]))      # 3
print(soma_maxima_subarray([-2, -3, -1, -4]))       # -1
print(soma_maxima_subarray([5, -2, 3, 4]))          # 10
print(soma_maxima_subarray([1, 2, 3, -10, 4, 5]))   # 9 (4+5)
