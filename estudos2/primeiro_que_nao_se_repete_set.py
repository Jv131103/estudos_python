def primeiro_nao_repetido(numeros):
    frequencias = {}

    # 1ª passagem: contar quantas vezes cada número aparece
    for numero in numeros:
        frequencias[numero] = frequencias.get(numero, 0) + 1

    # 2ª passagem: procurar o primeiro que apareceu uma única vez
    for numero in numeros:
        if frequencias[numero] == 1:
            return numero

    return None


def trata_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um valor numérico inteiro.")


def trata_quantidade(msg):
    while True:
        quantidade = trata_int(msg)

        if quantidade > 0:
            return quantidade

        print("Informe pelo menos 1 número.")


def trata_sim_nao(msg):
    while True:
        resposta = input(msg).strip().lower().replace("ã", "a")

        if resposta in ["sim", "nao"]:
            return resposta

        print("Digite apenas 'sim' ou 'nao'.")


def main():
    while True:
        quantidade = trata_quantidade(
            "Quantos números quer informar? "
        )

        numeros = []

        for i in range(quantidade):
            numero = trata_int(f"Número {i + 1}: ")
            numeros.append(numero)

        resultado = primeiro_nao_repetido(numeros)

        print()

        if resultado is None:
            print("Não existe número não repetido.")
        else:
            print(f"Primeiro número não repetido: {resultado}")

        print()

        continuar = trata_sim_nao(
            "Quer continuar? [sim | nao]: "
        )

        if continuar == "nao":
            break

        print()


if __name__ == "__main__":
    main()
