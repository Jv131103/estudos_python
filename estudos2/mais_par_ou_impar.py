def eh_par(number):
    return number % 2 == 0


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
        number = trata_int("Digite um número: ")
        resultado = "Par" if eh_par(number) else "Ímpar"
        print(f"O número {number} é {resultado}")
        novamente = trata_input("Novamente? [sim | nao] ")
        if novamente == "nao":
            break
        print()


if __name__ == "__main__":
    main()
