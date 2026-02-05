"""
Crie uma classe Animal com:

    nome

    espécie

    Crie um objeto e imprima os dados.
"""


class Animal:
    def __init__(self, nome, especie) -> None:
        self.nome = nome
        self.especie = especie


a1 = Animal("flufy", "Pinguin de Adélia")
print(a1.nome)
print(a1.especie)
