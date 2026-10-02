def terceiro_maior(lista):
    maior = lista[0]
    segundo = None
    terceiro = None

    for x in lista[1:]:

        if x > maior:
            terceiro = segundo
            segundo = maior
            maior = x

        elif x < maior:

            if segundo is None or x > segundo:
                terceiro = segundo
                segundo = x

            elif x < segundo:
                if terceiro is None or x > terceiro:
                    terceiro = x

    return maior, segundo, terceiro


def trata_int(msg):
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


def main():
    while True:
        while True:
            n = trata_int("Quantos números quer informar? ")

            if n >= 2:
                break

            print("Informe pelo menos 2 números.")

        lista = []

        for v in range(n):
            lista.append(trata_int(f"Número {v + 1}: "))

        print()

        maior, segundo, terceiro = terceiro_maior(lista)
        print(f"Maior número: {maior}")

        if segundo is None:
            print("Segundo maior número: Não existe")
        else:
            print(f"Segundo maior número: {segundo}")

        if terceiro is None:
            print("Terceiro maior número: Não existe")
        else:
            print(f"Terceiro maior número: {terceiro}")

        print()

        opc = trata_input("Novamente? [sim | nao] ")
        if opc == "nao":
            break


main()
