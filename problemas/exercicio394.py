class Retangulo:
    def __init__(self, largura, altura) -> None:
        if largura <= 0 or altura <= 0:
            raise ValueError(f"Um retângulo não existe com: {largura=} e {altura=}")
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def eh_quadrado(self):
        return self.largura == self.altura


ret = Retangulo(5, 5)
print(f"Area: {ret.area()}")
print(f"Perimetro: {ret.perimetro()}")
print(f"É Quadrado: {ret.eh_quadrado()}")
