class Votacao:
    def __init__(self) -> None:
        self.votos = {}

    def votar(self, nome):
        self.votos[nome] = self.votos.get(nome, 0) + 1

    def resultado(self):
        return dict(self.votos)  # cópia simples

    def vencedor(self):
        if not self.votos:
            return None

        maior = max(self.votos.values())
        empatados = [nome for nome, qtd in self.votos.items() if qtd == maior]

        if len(empatados) > 1:
            return "empate"
        return empatados[0]


urna = Votacao()
urna.votar("ana")
urna.votar("bia")
urna.votar("ana")
print(urna.resultado())   # {'ana': 2, 'bia': 1}
print(urna.vencedor())    # 'ana'
