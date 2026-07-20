from dataclasses import dataclass


# Definindo a nossa "struct" para representar cada faixa da tabela
@dataclass
class FaixaImposto:
    limite_maximo: float
    aliquota: float
    deducao: float
    descricao: str


def calcular_imposto_renda(renda: float):
    # Criando a tabela de decisão como uma lista de objetos (structs)
    tabela = [
        FaixaImposto(2000.00, 0.000, 0.00, "Até R$ 2.000,00 (Isento)"),
        FaixaImposto(3000.00, 0.075, 150.00, "R$ 2.000,01 até R$ 3.000,00"),
        FaixaImposto(4500.00, 0.150, 375.00, "R$ 3.000,01 até R$ 4.500,00"),
        FaixaImposto(6000.00, 0.225, 712.50, "R$ 4.500,01 até R$ 6.000,00"),
        FaixaImposto(float("inf"), 0.275, 1012.50, "Acima de R$ 6.000,00")
    ]

    # Iterando pelos objetos da tabela
    for faixa in tabela:
        if renda <= faixa.limite_maximo:
            imposto = (renda * faixa.aliquota) - faixa.deducao

            print(f"Renda: R$ {renda:.2f}")
            print(f"Faixa: {faixa.descricao}")
            print(f"Alíquota aplicada: {faixa.aliquota * 100:.1f}%")
            print(f"Imposto a pagar: R$ {imposto:.2f}")
            return


calcular_imposto_renda(5000.00)
