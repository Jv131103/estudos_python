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


class AnimalFactory:
    _tipos = {
        "cachorro": Cachorro,
        "gato": Gato,
    }

    @classmethod
    def criar(cls, especie, nome, raca):
        try:
            return cls._tipos[especie](nome, raca)
        except KeyError:
            raise ValueError("Tipo inválido")


animal = AnimalFactory.criar("gato", "Mimi", "Persa")
print(animal)
animal.falar()
