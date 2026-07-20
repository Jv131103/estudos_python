def verifica_erros_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso / Altura precisa ser maior que 0")
    if peso > 640 or altura > 2.72:
        raise ValueError("Peso / Altura precisa atingir ao limite máximo atingido por um humano")


def calcular_imc(peso, altura):
    verifica_erros_imc(peso, altura)
    return peso / altura**2


def classificar_imc(peso, altura):
    tabela = [
        (0, 18.5, "Abaixo do peso"),
        (18.5, 24.9, "Peso normal"),
        (25, 29.9, "Sobrepeso"),
        (30, 39.9, "Obesidade"),
        (39.9, float("inf"), "Obesidade Grave"),
    ]

    print("++" * 20)
    print(f"Peso: {peso:.1f} | altura: {altura:.2f}")
    imc = calcular_imc(peso, altura)
    print(f"IMC -> {imc:.2f}")

    for minimo, maximo, nome in tabela:
        if minimo <= imc < maximo:
            print("Retorno:", nome)
            break
    else:
        print("IMC fora de faixa conhecida!")

    print("++" * 20)


def trata_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite apenas números")
            print()
            continue


def trata_msg(msg, tipo):
    while True:
        valor = input(msg).lower().replace("ã", 'a').strip()
        if not valor:
            print(f"Não digite mensagens vazias para {tipo}!")
            print()
            continue
        elif valor not in ["sim", 'nao']:
            print("Digite apenas Sim ou Não!")
            print()
            continue
        return valor


def main():
    while True:
        try:
            print("--" * 20)
            peso = trata_float("Digite o seu peso em Kg: ")
            altura = trata_float("Digite a sua altura em M: ")

            classificar_imc(peso, altura)
            continuar = trata_msg("Continuar? [sim / nao] ", "continuar")
            if continuar == "nao":
                print()
                print("Encerrando execução...")
                break
            print()
        except ValueError as ve:
            print(ve)
            print()

    print("FIM!")


if __name__ == "__main__":
    main()
