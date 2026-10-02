def nao_se_repete(numeros):
    dicionario = {}

    for numero in numeros:
        dicionario[numero] = dicionario.get(numero, 0) + 1

    for chave, valor in dicionario.items():
        if valor <= 1:
            return chave

    return None


def trata_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um valor numérico inteiro")


def trata_input_pergunta(msg):
    while True:
        dado = input(msg).strip().lower().replace("ã", "a")
        if not dado:
            print("Digite algo...")
            continue

        if dado not in ["sim", "nao"]:
            print("Digite apenas valores 'sim' ou 'nao'")
            continue

        return dado


def trata_input_busca(msg):
    while True:
        dado = input(msg).strip().lower().replace("á", "a")
        if not dado:
            print("Digite algo...")
            continue

        if dado not in ["dict", "list"]:
            print("Digite apenas valores 'dict' ou 'list'")
            continue

        return dado


def main():
    while True:

        while True:
            n = trata_int("Quantos números quer informar? ")
            if n > 0:
                break

            print("Informe pelo menos 1 número.")

        lista = []

        for v in range(n):
            lista.append(trata_int(f"Número {v + 1}: "))

        print()

        menor_freq = nao_se_repete(lista)
        if menor_freq is None:
            print("Não existe número não repetido.")
        else:
            print(f"Primeiro menos frequentes: {menor_freq}")

        print()

        continuar = trata_input_pergunta("QUER CONTINUAR? ")
        if continuar == "nao":
            break

        print()


main()
