"""
Crie uma classe Funcionario com:

    variável de classe aumento = 1.1

    método de instância salario_final

    método de classe alterar_aumento
"""


class Funcionario:
    aumento = 1.1

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def salario_final(self):
        return self.salario * Funcionario.aumento

    @classmethod
    def alterar_aumento(cls, novo_valor):
        if novo_valor <= 1:
            raise ValueError("O aumento deve ser maior que 1")
        cls.aumento = novo_valor


f1 = Funcionario("Ana", 3000)
f2 = Funcionario("Carlos", 4000)

print(f1.salario_final())
print(f2.salario_final())

Funcionario.alterar_aumento(1.2)

print(f1.salario_final())
print(f2.salario_final())
