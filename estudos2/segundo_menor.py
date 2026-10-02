def segundo_menor(lista):
    menor = lista[0]
    segundo = None

    for x in lista[1:]:
        if x < menor:
            segundo = menor
            menor = x

        elif x > menor:
            if segundo is None or x < segundo:
                segundo = x

    if segundo is None:
        segundo = "Não existe"

    return segundo, menor


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

        segundo, menor = segundo_menor(lista)
        print(f"Menor número: {menor}")
        print(f"Segundo menor distinto: {segundo}")
        print()

        opc = trata_input("Novamente? [sim | nao] ")
        if opc == "nao":
            break


main()
