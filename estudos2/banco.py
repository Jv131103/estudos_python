def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:

        meio = (inicio + fim) // 2

        if lista[meio].cpf == alvo:
            return meio

        elif lista[meio].cpf < alvo:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1


def encontrou_erro_deposito(saldo):
    if saldo <= 0:
        print("Não é possível realizar deposito com valores menores ou iguais a 0")
        return True
    return False


def encontrou_erro_saque(saldo, saque):
    if saque <= 0:
        print("Valor inválido!")
        return True
    if saque % 10 != 0:
        print("Saque deve ser múltiplo de R$ 10,00!")
        return True
    if saque > saldo:
        print("Saldo insuficiente!")
        return True
    return False


def trata_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite apenas números")
            continue


def trata_msg(msg, tipo):
    while True:
        valor = input(msg)
        if not valor:
            print(f"Não digite mensagens vazias para {tipo}!")
            continue
        return valor


class Conta:
    LIMITE_SAQUES = 3

    def __init__(self, titular, cpf, saldo_inicial=0):
        self.titular = titular
        self.cpf = cpf
        self.__saldo = saldo_inicial
        self.extrato = []
        self._saques_realizados = 0

    def depositar(self, valor):
        if not encontrou_erro_deposito(valor):
            self.__saldo += valor
            print(f"✅ Depósito de R$ {valor:.2f} realizado!")
            self.extrato.append(f"[+] Depósito: R$ {valor:.2f} | Saldo: {self.saldo}")

    def sacar(self, valor):
        if self.LIMITE_SAQUES == self._saques_realizados:
            print("❌ Limite de 3 saques por sessão atingido!")
            return

        if not encontrou_erro_saque(self.saldo, valor):
            self.__saldo -= valor
            print(f"✅ Saque de R$ {valor:.2f} realizado!")
            self.extrato.append(f"[-] Saque: R$ {valor:.2f} | Saldo: {self.saldo}")
            self._saques_realizados += 1

    def exibir_extrato(self):
        print("===== EXTRATO =====")
        for retornos in self.extrato:
            print(retornos)
        print("===================")
        print(f"Saldo atual: {self.saldo:.2f}")

    @property
    def saldo(self):
        return self.__saldo


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def criar_conta(self, titular, cpf, saldo_inicial=0):
        conta = Conta(titular, cpf, saldo_inicial)
        self.contas.append(conta)

    def buscar_conta(self, cpf):
        ordenado = sorted(self.contas, key=lambda conta: conta.cpf)
        valor = busca_binaria(ordenado, cpf)
        if valor == -1:
            print("==" * 20)
            print("Conta não encontrada!")
            print("==" * 20)
            print()
            return

        conta = ordenado[valor]
        print()
        return conta

    def listar_contas(self):
        print("==" * 20)
        if not self.contas:
            print("Sem contas registradas!")
            return

        for dados in self.contas:
            print(f"titular.: {dados.titular}")
            print(f"cpf.....: {dados.cpf}")
            print(f"saldo...: {dados.saldo}")
            print()


def menu_conta(conta: Conta):
    print("===================")
    print(f"Bem vindo {conta.titular}")
    print("===================")
    opcoes = [
        ["1", "Depositar"],
        ["2", "Sacar"],
        ["3", "Extrato"],
        ["0", "Sair"]
    ]
    for num, opc in opcoes:
        print(f"[{num}] {opc}")

    print()
    while True:
        escolha = input(">> ")

        if escolha == "0":
            print("Saindo da conta!")
            break
        elif escolha == "1":
            valor = trata_float("Valor: ")
            conta.depositar(valor)
        elif escolha == "2":
            valor = trata_float("Valor: ")
            conta.sacar(valor)
        elif escolha == "3":
            conta.exibir_extrato()
        else:
            print("Opção inválida para conta")
        print()


def exibir_opcao(banco):
    print(f"======= {banco} =======")
    opcoes = [
        ["1", "Nova conta"],
        ["2", "Acessar conta"],
        ["3", "Listar contas"],
        ["0", "Sair"]
    ]

    for opcao, escolha in opcoes:
        print(f"[{opcao}] {escolha}")
    print()


def menu(banco):
    exibir_opcao(banco)

    banco = Banco(banco)
    while True:
        escolha = input(">> ")
        if escolha == "1":
            titular = trata_msg("Digite um titular: ", "titular")
            cpf = trata_msg("Digite um CPF: ", "CPF")
            banco.criar_conta(titular, cpf, saldo_inicial=0)
        elif escolha == "2":
            cpf = trata_msg("Digite um CPF: ", "CPF")
            conta = banco.buscar_conta(cpf)
            if conta is not None:
                print()
                menu_conta(conta)
            exibir_opcao(banco.nome)
        elif escolha == "3":
            banco.listar_contas()
        elif escolha == "0":
            print("Saindo do banco!")
            break
        else:
            print("Opção inválida para conta")

        print()


banco = Banco("Banco Py")
menu(banco.nome)
