import datetime


class Conta:
    def __init__(self, titular, saldo=0) -> None:
        self.titular = titular
        self.__saldo = saldo
        self.__extrato = []

    def depositar(self, valor):
        if valor <= 0:
            print("Impossível depositar valor menor ou igual a zero")
            return
        print(f"Depositando {valor} em {self.__saldo}")
        self.__saldo += valor
        data = datetime.datetime.today().strftime('%d/%m/%Y')
        self.__extrato.append([f"Depósito {data}", valor])
        return self.__saldo

    def sacar(self, valor):
        data = datetime.datetime.today().strftime('%d/%m/%Y')
        if self.__saldo == 0:
            print("Saldo Zerado!")
            self.__extrato.append([f"Saque de {valor} Negativado por saldo zerado em {data}", self.__saldo])
            return
        elif self.__saldo < 0:
            print("Saldo negativo, impossível sacar")
            self.__extrato.append([f"Saque de {valor} Negativado por saldo negativo em {data}", self.__saldo])
            return
        elif valor > self.__saldo:
            self.__extrato.append([f"Saque de {valor} Negativado por ser maior que o saldo atual em {data}", self.__saldo])
            print("Impossível sacar valor maior que seu saldo")
            print(f"Seu saldo: {self.__saldo}")
            return
        print(f"Sacando {valor} em {self.__saldo}")
        self.__extrato.append([f"Saque {data}", valor])
        self.__saldo -= valor
        return self.__saldo

    def retornar_saldo(self):
        print("==" * 30)
        print(f"|\t\t\tSaldo de {self.titular}\t\t\t   |")
        print("--" * 30)
        print(f"| R$ {self.__saldo:.2f} reais \t\t\t\t\t   |")
        print("==" * 30)

    def extrato(self):
        print("==" * 30)
        for operacao in self.__extrato:
            print(f'Operação: {operacao[0]}')
            print(f'Valor: R$ {operacao[1]:.2f}')
            print()
        print("==" * 30)


conta = Conta("João", 1000)
conta.retornar_saldo()
conta.depositar(1000)
conta.depositar(0)
conta.retornar_saldo()
conta.sacar(1500)
conta.sacar(1500)
conta.retornar_saldo()
conta.sacar(500)
conta.sacar(500)
conta.retornar_saldo()
conta.depositar(8000)
conta.retornar_saldo()
conta.extrato()
