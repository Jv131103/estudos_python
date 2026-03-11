class Fila:

    def __init__(self):
        self.dados = []

    def enqueue(self, valor):
        self.dados.append(valor)

    def dequeue(self):
        if not self.is_empty():
            return self.dados.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.dados[0]
        return None

    def is_empty(self):
        return len(self.dados) == 0


def atendimento():
    f = Fila()

    print("++" * 30)

    while True:
        print("Fila do banco, digite abaixo o status atual do cliente...")
        processo_atual = input().split()

        if not processo_atual:
            print("Digite um comando válido.")
            print("--" * 30)
            continue

        if processo_atual[0] == "fechar":
            print("Fechando o banco")
            print("--" * 30)

            while not f.is_empty():
                print(f"Saindo {f.dequeue()}")

            print()
            print("Sem clientes")
            print("--" * 30)
            print("Banco fechado!")
            print("--" * 30)
            break

        elif processo_atual[0] == "atender":
            cliente = f.dequeue()
            if cliente is None:
                print("Não há clientes na fila")
            else:
                print(f"Atendendo {cliente}")

        elif processo_atual[0] == "chegar":
            if len(processo_atual) < 2:
                print("Digite no formato: chegar <nome>")
            else:
                pessoa = processo_atual[1]
                f.enqueue(pessoa)
                print(f"{pessoa} entrou na fila")

        else:
            print("Comando inválido, digite apenas:")
            print("chegar <nome_pessoa>")
            print("atender")
            print("fechar")

        print("--" * 30)


def atendimento2():
    f = Fila()

    operacoes = [
        "chegar João",
        "chegar Maria",
        "atender",
        "chegar Pedro",
        "atender",
        "chegar Douglas",
        "atender",
        "atender",
    ]

    for op in operacoes:
        partes = op.split()

        if partes[0] == "chegar":
            f.enqueue(partes[1])

        elif partes[0] == "atender":
            cliente = f.dequeue()
            if cliente is not None:
                print(f"Atendendo {cliente}")


if __name__ == "__main__":
    atendimento2()
