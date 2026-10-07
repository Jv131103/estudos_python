def maior_sequencia_crescente(lista):
    anterior = 0
    maior_sequencia = []
    sequencia_atual = []

    for atual in range(1, len(lista)):
        if lista[anterior] < lista[atual]:
            sequencia_atual.append(lista[anterior])
        else:
            sequencia_atual.append(lista[anterior])
            if len(sequencia_atual) > len(maior_sequencia):
                maior_sequencia = sequencia_atual

            sequencia_atual = []
        anterior = atual

    sequencia_atual.append(lista[atual])
    if len(sequencia_atual) > len(maior_sequencia):
        maior_sequencia = sequencia_atual

    return maior_sequencia, len(maior_sequencia)


maior_seq, tam = maior_sequencia_crescente([2, 4, 7, 3, 5, 8, 10, 1, 2])
print(f"Maior sequência crescente: {maior_seq}")
print(f"Tamanho: {tam}")
