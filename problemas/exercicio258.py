class Retangulo:
    def __init__(self, altura, largura) -> None:
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura

    def perimetro(self):
        return 2 * (self.altura + self.largura)


ret = Retangulo(2, 4)
print(ret.area())
print(ret.perimetro())
