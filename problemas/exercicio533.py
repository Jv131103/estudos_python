"""
Faça uma função que:

    Receba uma lista de números

    Retorne o maior valor da lista

    Use divisão e conquista

Não use max() nem loops

Dica:

    Compare o maior da metade esquerda com o maior da metade direita
"""


def maior(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)  # fim exclusivo

    if fim - inicio == 1:
        return lista[inicio]

    meio = (inicio + fim) // 2

    maior_esq = maior(lista, inicio, meio)
    maior_dir = maior(lista, meio, fim)

    return maior_esq if maior_esq > maior_dir else maior_dir


lista = [2, 3, 4]
print(maior(lista))

lista2 = [4, 3, 2]
print(maior(lista2))

lista3 = [2, 4, 3]
print(maior(lista3))
