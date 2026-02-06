"""
Crie uma classe Pessoa com:

    atributo _idade

    property idade

    não permitir idade negativa
"""


class AgeError(Exception):
    pass


class Pessoa:
    def __init__(self, idade=0) -> None:
        self.idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Idade precisa ser um valor do tipo int")

        if valor < 0:
            raise AgeError("Idade não pode ser negativa")

        self._idade = valor

    def retornar_idade(self):
        return f"Idade atual: {self.idade}"


p1 = Pessoa()
p1.idade = 22
print(p1.retornar_idade())
