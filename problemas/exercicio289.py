class Contador:
    def __init__(self) -> None:
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def decrementar(self):
        self.contador -= 1

    def ver(self):
        print(self.contador)


c1 = Contador()
c1.incrementar()
c1.incrementar()
c1.incrementar()
c1.incrementar()
c1.decrementar()
c1.ver()
