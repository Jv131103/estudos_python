def frete_por_registro_tabela(regiao):
    fretes = {
        "norte": 45,
        "nordeste": 35,
        "centro-oeste": 30,
        "sudeste": 15,
        "sul": 20
    }

    return fretes.get(regiao)


def frete_por_registro_match(regiao):
    match regiao:
        case "norte":
            valor = 45
        case "nordeste":
            valor = 35
        case "centro-oeste":
            valor = 30
        case "sudeste":
            valor = 15
        case "sul":
            valor = 20
        case _:
            valor = None

    return valor


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
        valor = input(msg).lower().replace("_", '-').replace(" ", "-").strip()
        if not valor:
            print(f"Não digite mensagens vazias para {tipo}!")
            print()
            continue
        return valor


def main():
    while True:
        regiao = trata_msg("Digite uma região do Brasil [digite SAIR para sair]: ", "região")
        if regiao == "sair":
            break
        print("==" * 20)
        print("Analisando por tabela de decisão...")
        print()
        valor = frete_por_registro_tabela(regiao)
        if valor is None:
            print("Região inválida!")
        else:
            print(f"Valor retornado: R$ {valor:.2f} reais")
        print("--" * 20)
        print()
        print("==" * 20)
        print("Analisando por cases...")
        print()
        valor = frete_por_registro_match(regiao)
        if valor is None:
            print("Região inválida!")
        else:
            print(f"Valor retornado: R$ {valor:.2f} reais")
        print("--" * 20)
        print()


if __name__ == "__main__":
    main()
