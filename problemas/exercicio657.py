"""
Crie uma factory para criar:

    Cachorro

    Gato
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome, raca) -> None:
        self.nome = nome
        self.raca = raca

    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):
    def __init__(self, nome, raca) -> None:
        super().__init__(nome, raca)

    def __str__(self):
        return f"Cachorro: nome={self.nome}, raça={self.raca}"

    def falar(self):
        print(f"{self.nome} está latindo")


class Gato(Animal):
    def __init__(self, nome, raca) -> None:
        super().__init__(nome, raca)

    def __str__(self):
        return f"Gato: nome={self.nome}, raça={self.raca}"

    def falar(self):
        print(f"{self.nome} está miando")


animais = {
    "cachorro": Cachorro,
    "gato": Gato,
}


def executar(especie: str, nome: str, raca: str) -> None:
    try:
        animal = animais[especie](nome, raca)
        print(animal)
        animal.falar()
    except KeyError:
        raise ValueError("Tipo inválido")


executar("cachorro", "Brutus", "Fila Brasileiro")
executar("gato", "Junin", "Siamês")
