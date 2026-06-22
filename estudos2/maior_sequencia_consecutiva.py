def maior_sequencia_consecutiva(lista):
    # Se a lista estiver vazia, o tamanho é 0
    if not lista:
        return 0

    maior_seq = 1  # Guarda o nosso recorde global
    atual_seq = 1  # Guarda o tamanho da sequência que estamos olhando agora

    for i in range(1, len(lista)):
        # Verifica se o número atual é exatamente o anterior + 1
        if lista[i] == lista[i - 1] + 1:
            atual_seq += 1
        else:
            # A sequência quebrou! Vamos atualizar o recorde se a atual for maior
            maior_seq = max(maior_seq, atual_seq)
            # Reseta o contador atual para 1 (começando a nova sequência)
            atual_seq = 1

    # Uma última checagem para o caso da maior sequência ir até o final da lista
    return max(maior_seq, atual_seq)


# Teste do exercício
lista = [1, 2, 3, 7, 8, 10, 11, 12, 13]
print(f"Resultado: {maior_sequencia_consecutiva(lista)}")  # Saída: 4
