"""
Crie uma classe Produto com:

    nome

    preço

    método mostrar_preco()
"""


class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

    def mostrar_preco(self):
        print(f"Valor de {self.nome}:")
        print(f"\tR$ {self.preco:.2f} reais")


p1 = Produto("Carro", 88000.43)
p1.mostrar_preco()
