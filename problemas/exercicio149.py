class Pessoa:
    def __init__(self, nome, sobrenome, idade) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def __str__(self) -> str:
        return f"Pessoa(nome={self.nome}, sobrenome={self.sobrenome}, idade={self.idade})"

    def informacoes_pessoais(self):
        print(f"Dados de {self.nome}")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"Idade: {self.idade}")


p1 = Pessoa("João", "Justino", 22)
print(p1)
p1.informacoes_pessoais()
