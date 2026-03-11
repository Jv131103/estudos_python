class ImpressionError(Exception):
    pass


class FilaComPilha:
    def __init__(self) -> None:
        self.entrada = []
        self.saida = []

    def enqueue(self, valor):
        self.entrada.append(valor)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("fila vazia")

        if not self.saida:
            while self.entrada:
                self.saida.append(self.entrada.pop())

        return self.saida.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("fila vazia")

        if not self.saida:
            while self.entrada:
                self.saida.append(self.entrada.pop())

        return self.saida[-1]

    def is_empty(self):
        return len(self.entrada) == 0 and len(self.saida) == 0

    def size(self):
        return len(self.entrada) + len(self.saida)


def impressao_menu_interativo():
    fp = FilaComPilha()

    while True:
        comando = input("Opção de impressão: ").strip()

        if not comando:
            print("Digite um comando válido.")
            continue

        partes = comando.split()
        acao = partes[0].lower()

        if acao == "desligar":
            print("Desligando impressão...")
            while not fp.is_empty():
                print(f"{fp.dequeue()} não impresso!")
            print("Impressão limpa!")
            return

        elif acao == "imprimir":
            if len(partes) < 2:
                print("Arquivo de documento não encontrado")
            else:
                documento = partes[1]
                fp.enqueue(documento)

        elif acao == "executar":
            if len(partes) >= 2 and partes[1].lower().replace("ã", "a") == "impressao":
                try:
                    print(f"Imprimindo {fp.dequeue()}")
                except IndexError:
                    print("Fila de impressão vazia")
            else:
                print("Comando inválido")
                print("Digite apenas:")
                print("\timprimir <documento>")
                print("\texecutar impressão")
                print("\tdesligar")

        else:
            print("Comando inválido")
            print("Digite apenas:")
            print("\timprimir <documento>")
            print("\texecutar impressão")
            print("\tdesligar")


def impressao_menu_simulado():
    fp = FilaComPilha()

    operacoes = [
        "imprimir documentoA",
        "imprimir documentoB",
        "imprimir documentoC",
        "executar impressão",
        "executar impressão",
    ]

    for op in operacoes:
        partes = op.split()
        acao = partes[0].lower()

        if acao == "imprimir":
            fp.enqueue(partes[1])

        elif acao == "executar":
            try:
                documento = fp.dequeue()
                print(f"Imprimindo {documento}")
            except IndexError:
                print("Fila de impressão vazia")


if __name__ == "__main__":
    # impressao_menu_interativo()
    impressao_menu_simulado()
