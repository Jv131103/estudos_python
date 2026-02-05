"""
Crie uma classe Pessoa com:

    atributo nome

    método apresentar()
"""


class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome

    def apresentar(self):
        return f"Olá!\nMeu nome é {self.nome}"


p1 = Pessoa("Adenilson")
print(p1.apresentar())
