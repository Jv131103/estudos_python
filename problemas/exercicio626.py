"""
Crie uma classe Pessoa e uma função externa cumprimentar(pessoa).
"""


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade


def cumprimentar(pessoa: Pessoa, mensagem: str = "Olá") -> str:
    return f"{mensagem} {pessoa.nome}"


p1 = Pessoa("João", 22)
print(cumprimentar(p1))
