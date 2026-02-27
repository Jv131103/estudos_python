def realizar_desconto_viagem(valor_pacote, categoria, qtd_passageiros):
    tabela = {
        "economica": {2: 0.03, 3: 0.04, "4+": 0.05},
        "executiva": {2: 0.05, 3: 0.07, "4+": 0.08},
        "primeira_classe": {2: 0.10, 3: 0.15, "4+": 0.20},
    }

    if categoria not in tabela:
        print("Categoria inválida!")
        return

    if qtd_passageiros < 2:
        desconto = 0
    elif qtd_passageiros in (2, 3):
        desconto = tabela[categoria][qtd_passageiros]
    else:
        desconto = tabela[categoria]["4+"]

    valor_desconto = valor_pacote * desconto
    valor_liquido = valor_pacote - valor_desconto
    valor_medio = valor_liquido / qtd_passageiros

    print(f"Valor Bruto: R$ {valor_pacote:.2f}")
    print(f"Desconto: R$ {valor_desconto:.2f}")
    print(f"Valor Líquido: R$ {valor_liquido:.2f}")
    print(f"Valor Médio por viajante: R$ {valor_medio:.2f}")


realizar_desconto_viagem(100_000, "primeira_classe", 2)
