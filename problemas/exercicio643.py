"""
Crie uma classe Produto com:

atributo de classe imposto

método de classe alterar_imposto
"""


class Produto:
    imposto = 1.5

    @classmethod
    def alterar_imposto(cls, novo_imposto):
        cls.imposto = novo_imposto

    def retornar_imposto(self):
        return self.__class__.imposto


p1 = Produto()
print(p1.retornar_imposto())
p1.alterar_imposto(2)
print(p1.retornar_imposto())
