def tabela_imposto(renda):
    tabela = [
        [2000, 0.000, 0, "Até R$ 2.000,00 (Isento)"],
        [3000, 0.075, 150, "R$ 2.000,01 até R$ 3.000,00"],
        [4500, 0.150, 375, "R$ 3.000,01 até R$ 4.500,00"],
        [6000, 0.225, 712.50, "R$ 4.500,01 até R$ 6.000,00"],
        [float("inf"), 0.275, 1012.50, "Acima de R$ 6.000,00"]
    ]

    for limite_maximo, aliquota, deducao, nome_faixa in tabela:
        if renda <= limite_maximo:
            imposto = (renda * aliquota) - deducao

            print(f"Renda: R$ {renda:.2f}")
            print(f"Faixa: {nome_faixa}")
            print(f"Alíquota aplicada: {aliquota * 100:.1f}%")
            print(f"Imposto a pagar: R$ {imposto:.2f}")
            return  # Sai da função assim que encontra a faixa correta


tabela_imposto(2001)
