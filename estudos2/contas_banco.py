class Conta:
    def __init__(self, titular, cpf, saldo_inicial=0):
        self.titular = titular
        self.cpf = cpf
        self.__saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido!")
            return
        self.__saldo += valor
        self.extrato.append(f"[+] Depósito:  R$ {valor:.2f} | Saldo: R$ {self.saldo:.2f}")
        print(f"✅ Depósito de R$ {valor:.2f} realizado!")

    def sacar(self, valor):
        # Regra base — só valida saldo
        if valor <= 0:
            print("Valor inválido!")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente!")
            return False
        self.__saldo -= valor
        return True

    def exibir_extrato(self):
        # Método base — subclasses chamam com super()
        print("===== EXTRATO =====")
        for linha in self.extrato:
            print(linha)
        print("===================")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    @property
    def saldo(self):
        return self.__saldo


class ContaCorrente(Conta):
    LIMITE_SAQUES = 3
    TAXA_SAQUE = 5.0

    def __init__(self, titular, cpf, saldo_inicial=0):
        super().__init__(titular, cpf, saldo_inicial)  # chama o __init__ da Conta
        self._saques_realizados = 0

    def sacar(self, valor):
        if self._saques_realizados >= self.LIMITE_SAQUES:
            print("❌ Limite de 3 saques atingido!")
            return
        if valor % 10 != 0:
            print("Saque deve ser múltiplo de R$ 10,00!")
            return

        total = valor + self.TAXA_SAQUE  # desconta taxa junto

        # Chama o sacar() da classe base para validar saldo e debitar
        if super().sacar(total):
            self._saques_realizados += 1
            self.extrato.append(f"[-] Saque:     R$ {valor:.2f} + R$ {self.TAXA_SAQUE:.2f} taxa | Saldo: R$ {self.saldo:.2f}")
            print(f"✅ Saque de R$ {valor:.2f} realizado! (taxa R$ {self.TAXA_SAQUE:.2f})")

    def exibir_extrato(self):
        print("Tipo: Conta Corrente")
        print(f"Titular: {self.titular}")
        super().exibir_extrato()  # reutiliza o extrato da base


class ContaPoupanca(Conta):
    def sacar(self, valor):
        # Sem taxa, sem limite — só chama a base
        if super().sacar(valor):
            self.extrato.append(f"[-] Saque:     R$ {valor:.2f} | Saldo: R$ {self.saldo:.2f}")
            print(f"✅ Saque de R$ {valor:.2f} realizado!")

    def render_juros(self, taxa):
        juros = self.saldo * taxa
        self.depositar(juros)
        # Ajusta a última linha do extrato para identificar como juros
        self.extrato[-1] = f"[+] Juros {taxa * 100:.0f}%: R$ {juros:.2f} | Saldo: R$ {self.saldo:.2f}"
        print(f"💰 Juros de {taxa * 100:.0f}% aplicados: R$ {juros:.2f}")

    def exibir_extrato(self):
        print("Tipo: Conta Poupança")
        print(f"Titular: {self.titular}")
        super().exibir_extrato()


print("\n" + "==" * 30)
print("TESTANDO CONTA CORRENTE")
print("==" * 30)

cc = ContaCorrente("João", "111.111.111-11", saldo_inicial=500)

# Depósito normal
cc.depositar(200)           # ✅ saldo: 700

# Saque válido (desconta taxa de R$5)
cc.sacar(100)               # ✅ saldo: 595 (100 + 5 de taxa)

# Saque não múltiplo de 10
cc.sacar(35)                # ❌ deve barrar

# Mais 2 saques para atingir o limite
cc.sacar(50)                # ✅ saldo: 535 (2º saque)
cc.sacar(50)                # ✅ saldo: 475 (3º saque)
cc.sacar(50)                # ❌ limite atingido

# Depósito inválido
cc.depositar(-100)          # ❌ deve barrar

cc.exibir_extrato()


print("\n" + "==" * 30)
print("TESTANDO CONTA POUPANÇA")
print("==" * 30)

cp = ContaPoupanca("Maria", "222.222.222-22", saldo_inicial=1000)

# Saque sem taxa, sem limite
cp.sacar(200)               # ✅ saldo: 800
cp.sacar(200)               # ✅ saldo: 600
cp.sacar(200)               # ✅ saldo: 400
cp.sacar(200)               # ✅ saldo: 200 (4º saque — sem limite!)

# Saque maior que saldo
cp.sacar(500)               # ❌ saldo insuficiente

# Juros de 1%
cp.render_juros(0.01)       # ✅ saldo: 202

cp.exibir_extrato()


print("\n" + "==" * 30)
print("TESTANDO POLIMORFISMO")
print("==" * 30)

contas = [
    ContaCorrente("Pedro", "333.333.333-33", saldo_inicial=300),
    ContaPoupanca("Ana", "444.444.444-44", saldo_inicial=300),
]

# Mesmo comando, comportamentos diferentes
for conta in contas:
    print(f"\n→ Sacando R$50 de {conta.titular}:")
    conta.sacar(50)         # CC desconta taxa, CP não
