import math


class Vetor:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'

    def __rpr__(self):
        return f'(x,y,z)=({self.x},{self.y},{self.z})'

    def __add__(self, outro):
        x = self.x + outro.x
        y = self.y + outro.y
        z = self.z + outro.z
        return Vetor(x, y, z)

    def __sub__(self, outro):
        x = self.x - outro.x
        y = self.y - outro.y
        z = self.z - outro.z
        return Vetor(x, y, z)

    def __mul__(self, outro):
        x = self.x * outro.x
        y = self.y * outro.y
        z = self.z * outro.z
        soma = x + y + z
        return soma

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y and self.z == outro.z

    def __ne__(self, outro):
        return self.x != outro.x or self.y != outro.y or self.z != outro


vetor1 = Vetor(3, 4, 2)
vetor2 = Vetor(1, 1, 1)
print(vetor1 + vetor2)
print(vetor1 - vetor2)
print(vetor1 * vetor2)
print(abs(vetor1))
print(vetor1 == vetor2)
print(vetor1 != vetor2)
