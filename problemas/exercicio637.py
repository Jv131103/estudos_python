"""
Crie classes Cachorro e Gato com método falar
e chame ambos em um loop.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):
    def falar(self):
        return "Au au"


class Gato(Animal):
    def falar(self):
        return "Miau"


animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.falar())
