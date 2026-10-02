def trata_nota(msg):
    while True:
        try:
            nota = float(input(msg).replace(",", "."))

            if 0 <= nota <= 10:
                return nota

            print("Digite uma nota entre 0 e 10.")

        except ValueError:
            print("Digite apenas números")
            continue


def trata_qtd_notas(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um valor numérico inteiro")


def trata_input(msg):
    while True:
        dado = input(msg).strip().lower().replace("ã", "a")
        if not dado:
            print("Digite algo...")
            continue

        if dado not in ["sim", "nao"]:
            print("Digite apenas valores 'sim' ou 'nao'")
            continue

        return dado


def analisar_notas(lista):
    maior = lista[0]
    menor = lista[0]
    soma = 0
    for valor in lista:
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

        soma += valor

    media = soma / len(lista)
    qtd_acima_media = 0
    qtd_abaixo_media = 0
    qtd_iguais_media = 0

    for nota in lista:
        if nota > media:
            qtd_acima_media += 1
        elif nota < media:
            qtd_abaixo_media += 1
        else:
            qtd_iguais_media += 1

    return maior, menor, media, qtd_acima_media, qtd_abaixo_media, qtd_iguais_media


def main():
    while True:

        while True:
            n = trata_qtd_notas("Quantos números quer informar? ")
            if n > 0:
                break

            print("Informe pelo menos 1 número.")

        lista = []

        for v in range(n):
            lista.append(trata_nota(f"Número {v + 1}: "))

        print()

        maior, menor, media, qtd_acima_media, qtd_abaixo_media, qtd_iguais_media = analisar_notas(lista)

        print(f"Maior nota: {maior}")
        print(f"Menor nota: {menor}")
        print(f"Média: {media:.2f}")
        print(f"Notas acima da média: {qtd_acima_media}")
        print(f"Notas abaixo da média: {qtd_abaixo_media}")
        print(f"Notas iguais da média: {qtd_iguais_media}")
        print()

        opc = trata_input("Novamente? [sim | nao] ")
        if opc == "nao":
            break


main()
