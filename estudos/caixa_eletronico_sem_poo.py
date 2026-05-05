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


def depositar(saldo, extrato):
    valor = trata_float("Valor para depósito: ")
    if not encontrou_erro_deposito(valor):
        saldo += valor
        print(f"✅ Depósito de R$ {valor:.2f} realizado!")
        extrato.append(f"[+] Depósito: R$ {valor:.2f} | Saldo: {saldo}")
        return saldo


def sacar(saldo, extrato, saques_realizados):
    if saques_realizados >= 3:
        print("❌ Limite de 3 saques por sessão atingido!")
    else:
        valor = trata_float("Valor para saque: ")
        if not encontrou_erro_saque(saldo, valor):
            saldo -= valor
            print(f"✅ Saque de R$ {valor:.2f} realizado!")
            extrato.append(f"[-] Saque: R$ {valor:.2f} | Saldo: {saldo}")
            saques_realizados += 1

    return saldo, saques_realizados


def exibir_extrato(extrato, saldo):
    print("===== EXTRATO =====")
    for retornos in extrato:
        print(retornos)
    print("===================")
    print(f"Saldo atual: {saldo:.2f}")


def menu():
    opcoes = [
        ["1", "Depositar"],
        ["2", "Sacar"],
        ["3", "Extrato"],
        ["0", "Sair"]
    ]

    print("========== BANCO PY ==========")
    for num, opc in opcoes:
        print(f"[{num}] {opc}")
    extrato = []
    saldo = 1000
    saques = 0
    while True:
        escolha = input(">> ")

        if escolha == "0":
            print("Caixa fechado!")
            break
        elif escolha == "1":
            saldo = depositar(saldo, extrato)
        elif escolha == "2":
            saldo, saques = sacar(saldo, extrato, saques)
        elif escolha == "3":
            exibir_extrato(extrato, saldo)
        else:
            print("Opção inválida")
        print()


if __name__ == "__main__":
    menu()
