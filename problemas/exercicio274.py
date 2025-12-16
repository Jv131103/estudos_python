class Termometro:
    def __init__(self, temperatura=0) -> None:
        self.temperatura = temperatura

    def aumentar(self, valor):
        self.temperatura += valor

    def diminuir(self, valor):
        self.temperatura -= valor

    def ver(self):
        print(f"Status da temperatura: {self.temperatura:.1f} °C")


t = Termometro()
t.aumentar(10)
t.ver()
t.diminuir(11)
t.ver()
