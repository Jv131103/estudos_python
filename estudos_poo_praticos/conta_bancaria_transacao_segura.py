class ContaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo

    def transferir(self, valor: float, destino: "ContaBancaria"):
        if valor > self.saldo:
            raise ValueError(f"Saldo insuficiente na conta de {self.titular}.")
        self.saldo -= valor
        destino.saldo += valor

    def __repr__(self):
        return f"Conta({self.titular}, Saldo: R${self.saldo:.2f})"


class TransacaoSegura:
    def __init__(self, origem: ContaBancaria, destino: ContaBancaria):
        self.origem = origem
        self.destino = destino

    def __enter__(self):
        # Tira uma "foto" dos saldos antes de qualquer operação
        self._saldo_origem_backup = self.origem.saldo
        self._saldo_destino_backup = self.destino.saldo
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # Reverte as alterações se houve exceção (Rollback)
            self.origem.saldo = self._saldo_origem_backup
            self.destino.saldo = self._saldo_destino_backup
            print(f"\n[ROLLBACK] Erro detectado ({exc_val}). Saldos restaurados.")
        else:
            print("\n[COMMIT] Transação finalizada com sucesso.")

        # Retornar False garante que a exceção continue propagando para fora
        return False


conta1 = ContaBancaria("Alice", 100.0)
conta2 = ContaBancaria("Bob", 50.0)

with TransacaoSegura(conta1, conta2):
    conta1.transferir(40, conta2)

print(conta1)  # Conta(Alice, Saldo: R$60.00)
print(conta2)  # Conta(Bob, Saldo: R$90.00)
