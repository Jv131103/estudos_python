class PriorityQueue:
    def __init__(self):
        self.dados = []

    def push(self, valor, prioridade):
        self.dados.append((prioridade, valor))

    def pop(self):

        maior = 0

        for i in range(1, len(self.dados)):
            if self.dados[i][0] < self.dados[maior][0]:
                maior = i

        prioridade, valor = self.dados.pop(maior)
        return valor


def simular():
    opcoes = [
        "chegar João prioridade 3",
        "chegar Maria prioridade 1",
        "chegar Pedro prioridade 2"
    ]

    fp = PriorityQueue()

    print("Chegando pacientes:")
    for opcao in opcoes:
        informacoes = opcao.split()
        _, nome, _, prioridade = informacoes
        print(opcao)
        fp.push(nome, int(prioridade))

    print("Iniciando atendimento:")
    for _ in range(len(opcoes)):
        print(f"atender -> {fp.pop()}")


if __name__ == "__main__":
    simular()
