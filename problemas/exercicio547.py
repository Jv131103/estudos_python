"""
Faça um programa que:

    . Use uma tupla (x, y) para representar uma posição em um grid 2D

    . Use um dicionário onde:

        . a chave é a tupla (x, y)

        . o valor é um número inteiro (contador)

    . Simule algumas posições visitadas e incremente o contador

    . Mostre todas as posições visitadas e seus valores

Exemplo conceitual:

    (1, 2) → 3 visitas
    (0, 0) → 1 visita

DICAS

    Tuplas são imutáveis → podem ser chave

    Pense em (x, y) como coordenada

    Isso é base de jogos, mapas e memoização
"""


def criar_grid(x, y):
    return x, y


def gerar_dicionario(qtd_grids=1):
    d = {}

    for chave in range(qtd_grids + 1):
        for novo in range(qtd_grids + 1):
            valor = chave, novo
            d[valor] = 0

    return d


def acessar(dicionario, chave):
    if chave not in dicionario:
        print("Grid não existe!")
        return None
    dicionario[chave] = dicionario.get(chave, 0) + 1
    return dicionario


cont = 0

dicionario = gerar_dicionario(3)

print(dicionario)
while cont < 10:
    print("==" * 30)
    chave = (int(input("X: ")), int(input("Y: ")))
    atualizado = acessar(dicionario, chave)
    cont += 1
    print("==" * 30)

print(atualizado)
