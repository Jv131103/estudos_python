def maior_janela(lista, k):
    maior = 0
    maior_lista = []
    for i in range(len(lista) - k + 1):
        dados = lista[i:i + k]
        soma = 0

        for dado in dados:
            soma += dado

        if soma > maior:
            maior_lista = dados
            maior = soma

    return maior_lista, maior


def maior_janela_sliding(lista, k):
    if k <= 0 or k > len(lista):
        return None

    soma_atual = 0

    for i in range(k):
        soma_atual += lista[i]

    maior_soma = soma_atual
    inicio_maior = 0

    for direita in range(k, len(lista)):
        saiu = lista[direita - k]
        entrou = lista[direita]

        soma_atual = soma_atual - saiu + entrou

        if soma_atual > maior_soma:
            maior_soma = soma_atual
            inicio_maior = direita - k + 1

    janela = lista[inicio_maior:inicio_maior + k]

    return janela, maior_soma


lista = [4, 2, 7, 1, 8, 3]
k = 3

print(maior_janela(lista, k))
print(maior_janela_sliding(lista, k))
