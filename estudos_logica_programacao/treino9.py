from random import random


def gerar_matriz():
    matriz = []

    for i in range(100):
        lista = []

        for j in range(100):
            valor = round(random() * 1_000_000, 4)

            lista.append(valor)

        matriz.append(lista)

    return matriz


def somar_coluna_matriz_e_retornar_media(matriz):
    soma = 0
    coluna = int(input("Digite a coluna que vai realizar a soma: "))

    if not (0 <= coluna < len(matriz[0])):
        print("Coluna inválida.")
        return

    for i in range(len(matriz)):
        soma += matriz[i][coluna]

    media = soma / len(matriz)
    print("==" * 30)
    print(f"A soma da coluna {coluna} é {soma}")
    print(f"A media é {media:.4f}")
    print("==" * 30)


def somar_linha_matriz_e_retornar_media(matriz):
    soma = 0
    linha = int(input("Digite a linha que vai realizar a soma: "))

    if not (0 <= linha < len(matriz)):
        print("Linha inválida.")
        return

    for j in range(len(matriz[linha])):
        soma += matriz[linha][j]

    media = soma / len(matriz[linha])
    print("==" * 30)
    print(f"A soma da linha {linha} é {soma}")
    print(f"A media é {media:.4f}")
    print("==" * 30)


def coluna_cuja_media_seja_maior(matriz):
    maior_media = -1
    coluna_maior = -1

    for coluna in range(len(matriz[0])):   # agora percorre COLUNAS
        soma = 0

        for linha in range(len(matriz)):   # percorre LINHAS
            soma += matriz[linha][coluna]

        media = soma / len(matriz)

        if media > maior_media:
            maior_media = media
            coluna_maior = coluna

    print("==" * 30)
    print(f"Coluna com maior média: {coluna_maior}")
    print(f"Maior média: {maior_media}")
    print("==" * 30)


def linha_cuja_media_seja_maior(matriz):
    maior_media = -1
    linha_maior = -1

    for linha in range(len(matriz)):
        soma = 0
        for coluna in range(len(matriz[linha])):
            soma += matriz[linha][coluna]

        media = soma / len(matriz[linha])

        if media > maior_media:
            maior_media = media
            linha_maior = linha

    print("==" * 30)
    print(f"Linha com maior média: {linha_maior}")
    print(f"Maior média: {maior_media:.4f}")
    print("==" * 30)


def diagonal_maior_direita(matriz):

    soma = 0

    for i in range(len(matriz)):
        soma += matriz[i][i]

    media = soma / len(matriz)

    print("==" * 30)
    print(f"A soma da diagonal maior é: {soma}")
    print(f"Média: {media:.4f}")
    print("==" * 30)


def diagonal_maior_esquerda(matriz):
    soma = 0
    n = len(matriz)

    for i in range(n):
        soma += matriz[i][n - 1 - i]

    media = soma / n

    print("==" * 30)
    print(f"A soma da diagonal secundária é: {soma}")
    print(f"Média: {media:.4f}")
    print("==" * 30)


def main():

    matriz = gerar_matriz()

    opcoes = {
        '0': "encerrar",
        '1': "somar e extrair a média aritmética de uma determinada coluna.",
        '2': "somar e extrair a média aritmética de uma determinada linha.",
        '3': "achar a coluna cuja média seja maior.",
        '4': "achar a linha cuja média seja maior.",
        '5': "somar e extrair a média aritmética da diagonal maior (da célula superior esquerda para a inferior direita).",
        '6': "somar e extrair a média aritmética da diagonal maior (da célula superior direita para a célula inferior esquerda)."
    }
    while True:
        for key, value in opcoes.items():
            print(f"{key} - {value}")

        opc = input("Escolha uma opcao de 0 a 6: ")

        match opc:
            case '0':
                break
            case '1':
                somar_coluna_matriz_e_retornar_media(matriz)
            case '2':
                somar_linha_matriz_e_retornar_media(matriz)
            case '3':
                coluna_cuja_media_seja_maior(matriz)
            case '4':
                linha_cuja_media_seja_maior(matriz)
            case '5':
                diagonal_maior_direita(matriz)
            case '6':
                diagonal_maior_esquerda(matriz)
            case _:
                print("Opção inválida! Digite valores de 0 a 6")


main()
