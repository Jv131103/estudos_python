def maior(lista):
    maior = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior


def maior_versao_limpa(lista):
    return max(lista)


l1 = [1, 2, 3, 4]
print(maior(l1))
l2 = [1, 2, 3, 4]
print(maior(l2))
