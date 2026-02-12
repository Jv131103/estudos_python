"""
Crie uma dataclass Livro com:

    titulo

    autor

    preco
"""

from dataclasses import dataclass


@dataclass
class Livro:
    titulo: str
    autor: str
    preco: float

    def mostrar(self):
        print(self.titulo)
        print(self.autor)
        print(self.preco)


livro = Livro("Com quantos paus se faz uma canoa", "batata", 1200)
livro.mostrar()
