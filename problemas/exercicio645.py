"""
Crie uma classe abstrata Forma com método area()
e duas subclasses (Quadrado, Circulo).
"""

from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def area(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def area(self):
        return self.lado * self.lado


class Circulo(Forma):
    def __init__(self, raio) -> None:
        self.raio = raio
        self.pi = 3.1415

    def area(self):
        return self.pi * self.raio**2


formas = [Quadrado(5), Circulo(7)]

for f in formas:
    print(f.area())
