class Lampada:
    def __init__(self) -> None:
        self.ligada = False

    def ligar(self):
        if not self.ligada:
            self.ligada = True

    def desligar(self):
        if self.ligada:
            self.ligada = False

    def status(self):
        if not self.ligada:
            print("Status: Desligado")
        else:
            print("Status: Ligado")

        return self.ligada


lampada = Lampada()
lampada.status()
lampada.ligar()
lampada.status()
lampada.desligar()
lampada.status()
