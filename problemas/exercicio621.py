"""
Crie uma classe Carro com:

    variável de classe rodas = 4

    atributo modelo

    Crie dois objetos e imprima rodas.
"""


class Carro:
    rodas = 4

    def __init__(self, modelo) -> None:
        self.modelo = modelo

    def __str__(self):
        return f"modelo={self.modelo} | rodas={Carro.rodas}"


c1 = Carro("Civi LX 2000 1.6 automático")
print(c1)

c2 = Carro("GM Monza GL 2.0 1994 manual")
print(c2)
