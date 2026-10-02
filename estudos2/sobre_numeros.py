def maior_de3(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3


def menor_de3(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    else:
        return n3


def eh_par(number):
    return number % 2 == 0


def qtd_pares(a, b, c):
    lista = [a, b, c]
    pares = 0
    impares = 0
    for valor in lista:
        if eh_par(valor):
            pares += 1
        else:
            impares += 1

    return pares, impares


def soma(a, b, c):
    return a + b + c


def media(som):
    return som / 3


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
        n1 = trata_int("Valor de N1: ")
        n2 = trata_int("Valor de N2: ")
        n3 = trata_int("Valor de N3: ")

        print(f"Maior número: {maior_de3(n1, n2, n3)}")
        print(f"Menor número: {menor_de3(n1, n2, n3)}")
        som = soma(n1, n2, n3)
        print(f"Soma: {som}")
        print(f"Média: {media(som):.2f}")
        qtd_par, qtd_impar = qtd_pares(n1, n2, n3)
        print(f"Quantidade de números pares: {qtd_par}")
        print(f"Quantidade de números ímpares: {qtd_impar}")
        print()

        opc = trata_input("Novamente? [sim | nao] ")
        if opc == "nao":
            break


if __name__ == "__main__":
    main()
