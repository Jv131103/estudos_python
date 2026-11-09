def maior_sequencia_crescente(precos):
    if not precos:
        return {
            "tamanho": 0,
            "inicio": None,
            "fim": None
        }

    tamanho_atual = 1
    maior_tamanho = 1

    inicio_atual = 0
    melhor_inicio = 0
    melhor_fim = 0

    i = 1

    while i < len(precos):

        if precos[i] > precos[i - 1]:
            tamanho_atual += 1
        else:
            tamanho_atual = 1
            inicio_atual = i

        if tamanho_atual > maior_tamanho:
            maior_tamanho = tamanho_atual
            melhor_inicio = inicio_atual
            melhor_fim = i

        i += 1

    return {
        "tamanho": maior_tamanho,
        "inicio": melhor_inicio,
        "fim": melhor_fim
    }


print(maior_sequencia_crescente([10, 12, 15, 9, 11, 13, 14, 8]))
print(maior_sequencia_crescente([5, 4, 3, 2]))
print(maior_sequencia_crescente([1, 2, 3, 1, 2, 3]))
print(maior_sequencia_crescente([]))
