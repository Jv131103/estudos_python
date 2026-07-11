class ContaBancaria:
    def __init__(self, titular, saldo=0) -> None:
        if not titular or not titular.strip():
            raise ValueError("Titular não pode ser vazio")

        self.titular = titular
        self.__saldo = saldo

    def valor_menor_que_0(self, valor):
        return valor <= 0

    def valor_maior_saldo(self, valor):
        return valor > self.__saldo

    def depositar(self, valor):
        if self.valor_menor_que_0(valor):
            raise ValueError("Não é possível depositar valor negativo")

        print(f"Saldo depositado: R$ {valor:.2f} reais")
        self.__saldo += valor

    def sacar(self, valor):
        if self.valor_menor_que_0(valor):
            raise ValueError("Não é possível sacar valor negativo")

        if self.valor_maior_saldo(valor):
            raise ValueError("Não é possível sacar valor maior que o saldo")

        print(f"Saldo sacado: R$ {valor:.2f} reais")
        self.__saldo -= valor


if __name__ == "__main__":
    c1 = ContaBancaria("João", 36578)
    c1.sacar(100)
    c1.depositar(100)
    c1.depositar(-1)
    c1.depositar(100)
    c1.sacar(50)
    c1.sacar(1000)
