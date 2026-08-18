class Funcionario:
    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self._salario = salario

    def calcular_salario(self):
        return self._salario


class Gerente(Funcionario):
    def __init__(self, nome, salario) -> None:
        super().__init__(nome, salario)

    def calcular_salario(self):
        return self._salario + 1500


class Vendedor(Funcionario):
    def __init__(self, nome, salario, vendas, percentual_comissao) -> None:
        super().__init__(nome, salario)
        self.vendas = vendas
        self.percentual_comissao = percentual_comissao

    def calcular_salario(self):
        return self._salario + self.vendas * self.percentual_comissao


funcionarios = [
    Funcionario("Carlos", 3000),
    Gerente("Ana", 5000),
    Vendedor("Bruno", 2000, vendas=10000, percentual_comissao=0.05)
]

for f in funcionarios:
    print(f"{f.nome}: R$ {f.calcular_salario():.2f}")
