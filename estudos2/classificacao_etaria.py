from dataclasses import dataclass


@dataclass
class FaixaEtaria:
    idade_min: int
    idade_max: int
    categoria: str
    desconto: str


def classificacao_etaria(idade_cliente):
    if idade_cliente < 0:
        raise ValueError("Idade inválida!")

    if idade_cliente > 122:
        raise ValueError("Idade acima do limite máximo já registrado para um ser humano")

    tabela_eca = [
        FaixaEtaria(0, 5, "Criança (colo)", "Isento"),
        FaixaEtaria(6, 11, "Criança", "50%"),
        FaixaEtaria(12, 17, "Adolescente", "50% (com carteira estudantil)"),
        FaixaEtaria(18, 59, "Adulto", "0%"),
        FaixaEtaria(60, 122, "Idoso", "50%"),
    ]

    print("==" * 30)
    for faixa in tabela_eca:
        if faixa.idade_min <= idade_cliente <= faixa.idade_max:
            print(f"Idade: {idade_cliente}")
            print(f"categoria: {faixa.categoria}")
            print(f"desconto: {faixa.desconto}")
            break

    print()
    print("--" * 30)


def trata_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um valor numérico inteiro")


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
            print("==" * 30)
            idade_cliente = trata_int("Digite a sua idade: ")

            classificacao_etaria(idade_cliente)

            denovo = trata_msg("Nova consulta: [SIM | NAO] ", "NOVA_CONSULTA")
            if denovo == "nao":
                print("--" * 30)
                print("Encerrando o sistema...")
                break
            print()
        except ValueError as ve:
            print(ve)
            print()


if __name__ == "__main__":
    main()
