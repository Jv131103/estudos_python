"""
Crie uma classe Conta com:

    atributo de classe limite = 1000

    property saldo

    impedir saldo negativo
"""


class BalanceNegativeError(Exception):
    pass


class LimitError(Exception):
    pass


class Conta:
    limite = 1000

    def __init__(self, saldo=0.0) -> None:
        self.saldo = saldo  # usa o setter

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("Saldo deve ser numérico")

        if valor < 0:
            raise BalanceNegativeError("Saldo não pode ser negativo")

        if valor > Conta.limite:
            raise LimitError("Saldo não pode ultrapassar o limite da conta")

        self._saldo = valor


c1 = Conta(1000)
print(c1.saldo)
