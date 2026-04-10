class Telemetria:
    def __init__(self):
        self.eventos = []

    def registrar(self, evento):
        self.eventos.append(evento)

    def enviar(self):
        print("Enviando eventos:", self.eventos)
        self.eventos = []


telemetria = Telemetria()

telemetria.registrar("clique_botao_comprar")
telemetria.registrar("busca_tenis")
telemetria.enviar()
