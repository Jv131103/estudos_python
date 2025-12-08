class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def criar_anonimo(cls):
        return cls("Anônimo")


p = Pessoa.criar_anonimo()
print(p.nome)
