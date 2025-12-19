class Termostato:
    def __init__(self) -> None:
        self.temperatura = 0

    def aumentar(self, valor):
        self.temperatura += valor

    def diminuir(self, valor):
        self.temperatura -= valor

    def status(self):
        if self.temperatura == 0:
            print("Desligado")
        elif self.temperatura <= 18:
            print("Frio")
        elif self.temperatura <= 25:
            print("Ok")
        else:
            print("Quente")


t = Termostato()
t.status()
t.aumentar(18)
t.status()
t.aumentar(18)
t.status()
t.diminuir(12)
t.status()
