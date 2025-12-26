class Cronometro:
    def __init__(self):
        self.rodando = False
        self.tempo = 0

    def iniciar(self):
        self.rodando = True

    def parar(self):
        self.rodando = False

    def zerar(self):
        self.tempo = 0

    def tick(self, segundos=1):
        if self.rodando:
            self.tempo += segundos


c = Cronometro()
c.tick(5)      # parado: não soma
c.iniciar()
c.tick(5)      # soma 5
c.parar()
c.tick(10)     # parado: não soma
print(c.tempo)  # 5
