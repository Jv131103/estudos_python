class HistoricoComLimite:
    def __init__(self, limite) -> None:
        self.capacidade = limite
        self.historico = []

    def cheia(self):
        return len(self.historico) == self.capacidade

    def entrar(self, valor):
        if self.cheia():
            self.historico.pop(0)

        self.historico.append(valor)

    def __str__(self):
        return f"Histórico({self.historico})"


dados = HistoricoComLimite(3)
dados.entrar(1)
dados.entrar(2)
dados.entrar(3)
print(dados)
dados.entrar(4)
print(dados)
