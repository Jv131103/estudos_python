import datetime


class Conta:
    def __init__(self, nome_titular, numero_conta, saldo=0.0) -> None:
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
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

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor de depósito não pode ser negativo ou zero.")
            self._registrar("depósito com erro", valor, "valor inválido")
            return False

        self.__saldo += valor
        self._registrar("depósito", valor)
        return True

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor de saque não pode ser negativo ou zero.")
            self._registrar("saque com erro", valor, "valor inválido")
            return False

        if valor > self.__saldo:
            print("Saldo insuficiente.")
            self._registrar("saque com erro", valor, "saldo insuficiente")
            return False

        self.__saldo -= valor
        self._registrar("saque", valor)
        return True

    def transferir_para(self, outra_conta: "Conta", valor: float) -> bool:
        if not isinstance(outra_conta, Conta):
            raise ValueError("outra_conta precisa ser uma instância de Conta")

        if not self.sacar(valor):
            self._registrar("transferência com erro", valor, f"para {outra_conta.nome_titular}")
            return False

        outra_conta.depositar(valor)
        self._registrar("transferência", valor, f"para {outra_conta.nome_titular}")
        return True

    def extrato_bancario(self):
        print("==" * 20)
        print(f"EXTRATO DE {self.nome_titular} (Conta {self.numero_conta})")
        print("==" * 20)
        if not self.extrato:
            print("Nenhuma movimentação.")
        for linha in self.extrato:
            print(linha)
        print("==" * 20)

    def ver_saldo(self):
        print("==" * 10)
        print(f"Titular: {self.nome_titular}")
        print(f"Conta: {self.numero_conta}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("==" * 10)


class Banco:
    def __init__(self) -> None:
        self.contas = []

    def is_account(self, conta):
        return isinstance(conta, Conta)

    def adicionar_conta(self, conta):
        if not self.is_account(conta):
            print("Conta inválida!")
            return False

        # opcional: impedir contas duplicadas por número
        if self.buscar_conta(conta.numero_conta) is not None:
            print(f"Já existe conta com número {conta.numero_conta}.")
            return False

        self.contas.append(conta)
        return True

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero_conta == numero:
                return conta
        return None

    def transferir(self, numero_origem, numero_destino, valor) -> bool:
        origem = self.buscar_conta(numero_origem)
        destino = self.buscar_conta(numero_destino)

        if origem is None:
            print(f"Conta de origem {numero_origem} não encontrada.")
            return False

        if destino is None:
            print(f"Conta de destino {numero_destino} não encontrada.")
            return False

        return origem.transferir_para(destino, valor)


# =========================
# Demonstração de uso
# =========================
c1 = Conta("Renato", 1, 500)
c2 = Conta("João", 2, 300)

b = Banco()
b.adicionar_conta(c1)
b.adicionar_conta(c2)

print("Transferindo 200 de Renato -> João")
ok = b.transferir(1, 2, 200)
print("Sucesso?", ok)
print("Saldos:", c1.saldo, c2.saldo)  # 300 / 500

print("\nTentando transferir 999 (deve falhar)")
ok = b.transferir(1, 2, 999)
print("Sucesso?", ok)
print("Saldos:", c1.saldo, c2.saldo)  # deve continuar 300 / 500

print("\nExtratos:")
c1.extrato_bancario()
c2.extrato_bancario()
