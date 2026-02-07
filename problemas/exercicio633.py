"""
Crie:

    classe Motor

    classe Carro usando composição
"""


class Motor:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        if self.ligado:
            print("Engasgando arranque, cuidado para não pifar")
        else:
            print("Ligando motor")
            self.ligado = True
        return self.ligado

    def desligar(self):
        if not self.ligado:
            print("Motor já desligado")
        else:
            print("Deligando motor")
            self.ligado = False
        return self.ligado


class Carro:
    def __init__(self, marca, modelo, ano, cor) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.motor = Motor()

    def ligar(self):
        if self.motor.ligar():
            print("Carro pronto para andar")

    def desligar(self):
        if not self.motor.desligar():
            print("Carro desligado")


carro = Carro("Honda", "Civic Lx auto 1.6", 2000, "Verde floresta")
carro.ligar()
carro.ligar()
carro.desligar()
carro.desligar()
