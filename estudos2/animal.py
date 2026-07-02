class Animal:
    def __init__(self, nome, especie, idade) -> None:
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def apresentar(self):
        print(f"Olá, sou {self.nome}, um(a) {self.especie} de {self.idade} anos")

    def fazer_aniversario(self):
        self.idade += 1


a = Animal("Rex", "cachorro", 3)
a.apresentar()
a.fazer_aniversario()
a.apresentar()
