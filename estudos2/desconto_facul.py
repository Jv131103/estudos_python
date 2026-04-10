def desconto_cupom1():
    valor_compra = float(input("Valor da compra: "))
    cupom = input("Cupom selecionado (FIAP10, PYTHON20): ").strip().upper()

    if cupom == "FIAP10":
        percent = 0.1
    elif cupom == "PYTHON20":
        percent = 0.2
    else:
        percent = 0.0
        print("Sem desconto! Cupom inválido!")

    format_text = "com desconto" if percent else "sem desconto"

    desconto = valor_compra - (valor_compra * percent)
    print(f"Valor final {format_text}: R$ {desconto:.2f}")


def desconto_cupom2():
    valor_compra = float(input("Valor da compra: "))
    cupom = input("Cupom selecionado (FIAP10, PYTHON20): ").strip().upper()

    format_text = "com desconto"
    opcoes = {
        "FIAP10": 0.1,
        "PYTHON20": 0.2
    }

    desconto = valor_compra - (valor_compra * opcoes.get(cupom, 0))
    if desconto == valor_compra:
        print("Sem desconto! Cupom inválido!")
        format_text = "sem desconto"

    print(f"Valor final {format_text}: R$ {desconto:.2f}")


desconto_cupom1()
desconto_cupom2()
