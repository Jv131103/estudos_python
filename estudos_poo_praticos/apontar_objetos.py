class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.melhor_amigo = None


def apresentar_cadeia_de_amizade(pessoa):
    if not isinstance(pessoa, Pessoa):
        raise TypeError("pessoa precisa ser do tipo Pessoa")

    people = pessoa

    while people:
        print(people.nome)
        people = people.melhor_amigo


ana = Pessoa("Ana")
bruno = Pessoa("Bruno")
carla = Pessoa("Carla")

ana.melhor_amigo = bruno
bruno.melhor_amigo = carla

apresentar_cadeia_de_amizade(ana)
