"""
Faça um programa que:

    Receba uma lista de números

    Tente calcular a média da lista

    Se a lista estiver vazia:

        use 0 como fallback

        Mostre o resultado final

Exemplo conceitual:

    Entrada: [10, 20, 30] → Média: 20
    Entrada: []           → Média: 0
"""


def media_lista1(lista):
    return sum(lista) / len(lista) if lista else 0


def media_lista2(lista):
    if not lista:
        return 0

    soma = 0

    for dados in lista:
        soma += dados

    return soma / len(lista)


def media_lista3(lista):
    if len(lista) <= 0:
        return 0

    soma = 0
    qtd = 0

    for dados in lista:
        soma += dados
        qtd += 1

    return soma / qtd


testes = [
    [10, 20, 30],
    []
]

for teste in testes:
    print(f"Média: {media_lista1(teste)}")
    print(f"Média: {media_lista2(teste)}")
    print(f"Média: {media_lista3(teste)}")
    print()
