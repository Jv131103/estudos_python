import datetime


class ContaBancaria:
    def __init__(self, nome_titular, saldo=0.0) -> None:
        self.nome_titular = nome_titular
        self.__saldo = float(saldo)
        self.extrato = []

    @property
    def saldo(self):
        return self.__saldo

    def _registrar(self, tipo, valor, mensagem_extra=""):
        agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        registro = (
            f"[{tipo.upper()} {agora} - {self.nome_titular}] "
            f"R$ {valor:.2f} | SALDO ATUAL: R$ {self.saldo:.2f}"
        )
        if mensagem_extra:
            registro += f" | {mensagem_extra}"
        self.extrato.append(registro)

    def depositar(self, valor: float):
        if valor <= 0:
            print("Valor de depósito não pode ser negativo ou zero.")
            self._registrar("depósito com erro", valor, "valor inválido")
            return

        self.__saldo += valor
        self._registrar("depósito", valor)

    def sacar(self, valor: float):
        if valor <= 0:
            print("Valor de saque não pode ser negativo ou zero.")
            self._registrar("saque com erro", valor, "valor inválido")
            return

        if valor > self.__saldo:
            print("Saldo insuficiente.")
            self._registrar("saque com erro", valor, "saldo insuficiente")
            return

        self.__saldo -= valor
        self._registrar("saque", valor)

    def extrato_bancario(self):
        print("==" * 20)
        print(f"EXTRATO DE {self.nome_titular}")
        print("==" * 20)
        if not self.extrato:
            print("Nenhuma movimentação.")
        for linha in self.extrato:
            print(linha)
        print("==" * 20)

    def ver_saldo(self):
        print("==" * 10)
        print(f"Titular: {self.nome_titular}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("==" * 10)


# Exemplo de uso
c = ContaBancaria("Renato")
c.depositar(100)
c.sacar(40)
c.ver_saldo()
c.extrato_bancario()
