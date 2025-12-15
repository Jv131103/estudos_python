class Conta:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Tipo inválido, valor precisa ser maior que 0")
            return False
        print(f"Atribuindo R$ {valor:.2f} ao saldo")
        self.__saldo += valor
        return True

    def ver_saldo(self):
        print("==" * 30)
        print(f"Saldo atual: R$ {self.__saldo:.2f}")
        print("==" * 30)


c1 = Conta(100)
c1.depositar(0)
c1.depositar(-1)
c1.depositar(200)
c1.ver_saldo()
