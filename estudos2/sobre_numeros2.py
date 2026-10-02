def devolver_informacoes(lista):
    maior = lista[0]
    menor = lista[0]

    soma = 0

    pares = impares = 0

    for i in range(0, len(lista)):
        if lista[i] > maior:
            maior = lista[i]

        if lista[i] < menor:
            menor = lista[i]

        if lista[i] % 2 == 0:
            pares += 1
        else:
            impares += 1

        soma += lista[i]

    media = soma / len(lista)

    return maior, menor, soma, media, pares, impares


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

            if n > 0:
                break

            print("Informe uma quantidade maior que zero.")

        lista = []

        for v in range(n):
            lista.append(trata_int(f"Número {v + 1}: "))

        print()
        maior, menor, soma, media, pares, impares = devolver_informacoes(lista)

        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}")
        print(f"Soma: {soma}")
        print(f"Média: {media:.2f}")
        print(f"Quantidade de números pares: {pares}")
        print(f"Quantidade de números ímpares: {impares}")
        print()

        opc = trata_input("Novamente? [sim | nao] ")
        if opc == "nao":
            break


if __name__ == "__main__":
    main()
