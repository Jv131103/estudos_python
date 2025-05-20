"""
Baseando-se nos exercícios passados, monte um dicionário com os seguintes
chaves:

    lista, somatorio, tamanho, maior e menor valor
"""


def exibir(lista, opcao="all"):
    dicionario = {
        "lista": lista,
        "somatorio": sum(lista),
        "tamanho": len(lista),
        "maior_valor": max(lista),
        "menor_valor": min(lista)
    }
    if dicionario.get(opcao):
        print(dicionario[opcao])
    else:
        print("DEFAULT")
        print(dicionario)


lista = [1, 2, 3, 4, 5]
exibir(lista)
exibir(lista, "lista")
exibir(lista, "somatorio")
exibir(lista, "tamanho")
exibir(lista, "maior_valor")
exibir(lista, "menor_valor")
exibir(lista, "batata")
