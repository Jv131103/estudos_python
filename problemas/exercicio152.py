class Lampada:
    def __init__(self, cor, voltagem, luminosidade) -> None:
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def ligado(self):
        return self.__ligada

    def ligar(self):
        if not self.ligado():
            print("Ligando a lâmpada")
            self.__ligada = True
        else:
            print("Lâmpada já está ligada")

    def desligar(self):
        if self.ligado():
            print("Desligando a lâmpada")
            self.__ligada = False
        else:
            print("Lâmpada já está desligada")

    def __str__(self) -> str:
        return f"Lampada({self.__cor}) - {self.__voltagem} Wts | Nível {self.__luminosidade}"


lampada_fluor = Lampada("clara", 2500, "Alta")
print(lampada_fluor)
lampada_fluor.desligar()
lampada_fluor.ligar()
lampada_fluor.ligar()
lampada_fluor.desligar()
lampada_fluor.desligar()
