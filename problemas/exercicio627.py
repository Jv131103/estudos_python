"""
Crie uma classe Produto que use uma função externa para calcular desconto.
"""


class Produto:
    def __init__(self, valor, regra_desconto):
        self.valor = valor
        self.regra_desconto = regra_desconto

    def aplicar_desconto(self):
        return self.regra_desconto(self.valor)


def desconto_15(valor):
    return valor * 0.85


prod = Produto(2000, desconto_15)
print(prod.aplicar_desconto())
