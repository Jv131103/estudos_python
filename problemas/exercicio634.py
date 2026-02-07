"""
Crie:

    classe base Funcionario

    classe Gerente herdando
"""


class Funcionario:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.salario_base = 1800

    def salario(self):
        return self.salario_base

    def relatorio(self):
        print(f"Nome: {self.nome}")
        print(f"CARGO: {self.__class__.__name__}")
        print(f"Salário: {self.salario():.2f}")


class Gerente(Funcionario):
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.aumento_percentual = 0.10  # 10%

    def salario(self):
        return self.salario_base * (1 + self.aumento_percentual)


ger1 = Gerente("IRINEU")
ger1.relatorio()

print()

func1 = Funcionario("Tadeu")
func1.relatorio()
