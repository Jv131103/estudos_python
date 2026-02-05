"""
Crie uma classe Conta com:

    saldo
    métodos depositar e sacar
"""


class errobancario(Exception):
    pass


class InvalidBalanceError(errobancario):
    pass


class InsufficientBalanceError(errobancario):
    pass


class Conta:
    def __init__(self, saldo=0.0) -> None:
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise InvalidBalanceError("DEPÓSITO NÃO PODE SER MENOR OU IGUAL A 0")

        self.saldo += valor
        return True

    def sacar(self, valor):
        if valor <= 0:
            raise InvalidBalanceError("SAQUE NÃO PODE SER MENOR OU IGUAL A 0")
        elif valor > self.saldo:
            raise InsufficientBalanceError("SAQUE NÃO PODE SER MAIOR QUE O SALDO ATUAL")

        self.saldo -= valor

    def __str__(self):
        return f"Conta(saldo={self.saldo})"


c1 = Conta()
c1.depositar(1000)
c1.sacar(1000)
print(c1)
