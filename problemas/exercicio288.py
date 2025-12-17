class Porta:
    def __init__(self) -> None:
        self.aberta = False

    def esta_aberto(self):
        return self.aberta

    def abrir(self):
        if not self.esta_aberto():
            self.aberta = True

    def fechar(self):
        if self.esta_aberto():
            self.aberta = False

    def status(self):
        return "aberto" if self.esta_aberto() else "fechado"


porta = Porta()
porta.abrir()
print(porta.status())
porta.fechar()
print(porta.status())
