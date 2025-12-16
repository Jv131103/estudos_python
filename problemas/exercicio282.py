class ContaBancaria:
    def __init__(self, saldo=0, juros=0) -> None:
        self.saldo = saldo
        self.juros = juros / 100

    def depositar(self, valor):
        if valor <= 0:
            print("Valor menor que 0 não será adicionado ao depósito")
            return

        print(f"Inserindo R$ {valor:.2f} a conta")
        self.saldo += valor
        self.__aplicar_juros()

    def __aplicar_juros(self):
        self.saldo += (self.saldo * self.juros)

    def ver_saldo(self):
        print("Extrato:")
        print(f"R$ {self.saldo:.2f} reais")


c = ContaBancaria(juros=2)
c.depositar(200)
c.ver_saldo()
