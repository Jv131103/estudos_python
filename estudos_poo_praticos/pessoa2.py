class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise ValueError("Tipo inválido para nome")

        if not nome:
            raise ValueError("Nome inválido")

        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if not isinstance(idade, int):
            raise ValueError("Tipo inválido para idade")

        if not (0 <= idade <= 150):
            raise ValueError("Idade inválida")

        self._idade = idade


p = Pessoa("Ana", 25)
print(p.nome)
p.idade = 200
p.nome = ""
