class Pessoa:
    def __init__(self, nome, idade, telefone) -> None:
        self.nome = nome
        self.idade = idade
        self._telefone = telefone

    def __str__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade}, telefone={self._telefone})"

    def resumo(self):
        print()
        print(f"Nome.....: {self.nome}")
        print(f"Idade....: {self.idade}")
        print(f"Telefone.: {self._telefone}")
        print()


class PessoaUniversidade(Pessoa):
    def __init__(self, nome, idade, telefone, universidade) -> None:
        super().__init__(nome, idade, telefone)
        self.universidade = universidade

    def __str__(self):
        return (
            f"Pessoa(nome={self.nome}, idade={self.idade}, telefone={self._telefone})"
            + f" - Universidade({self.universidade})"
        )

    def resumo(self):
        print()
        print(f"Nome.........: {self.nome}")
        print(f"Idade........: {self.idade}")
        print(f"Telefone.....: {self._telefone}")
        print(f"Universidade.: {self.universidade}")
        print()


pessoa_comum = Pessoa("Irineu", 21, '11 998765444')
print(pessoa_comum)
pessoa_comum.resumo()

print()

pessoa_estudante = PessoaUniversidade("João", 22, '11 989898123', "MIT")
print(pessoa_estudante)
pessoa_estudante.resumo()
