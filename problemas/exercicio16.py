"""
Faça um programa, com uma função, que calcula a média de uma lista.

Funções embutidas que podem te ajudar:

    . len(lista) = calcula o tamanho da lista

    . sum(lista) = Faz o somatório dos valores

"""


def media(*notas):
    return sum(notas) / len(notas)


def media2(notas):
    return sum(notas) / len(notas)


def media3(*notas):
    soma = 0
    qtd = 0
    for numero in notas:
        soma += numero
        qtd += 1

    media = soma / qtd
    return media


def media4(notas):
    soma = 0
    qtd = 0
    for numero in notas:
        soma += numero
        qtd += 1

    media = soma / qtd
    return media


if __name__ == "__main__":
    print(f"Media versão 1: {media(5, 5, 5, 5):.1f}")
    print(f"Media versão 2: {media2([5, 5, 5, 5]):.1f}")
    print(f"Media versão 3: {media3(5, 5, 5, 5):.1f}")
    print(f"Media versão 4: {media4([5, 5, 5, 5]):.1f}")
