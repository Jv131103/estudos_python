class Funcionario:
    def __init__(self, nome, salario=0.0) -> None:
        self.nome = nome
        self.salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if not isinstance(novo_salario, (int, float)) or isinstance(novo_salario, bool):
            raise TypeError("Tipo inválido para novo_salario, ele precisa ser do tipo INT / FLOAT")

        if novo_salario < 0:
            raise ValueError("novo_salario não pode ser negativo")

        self.__salario = novo_salario

    def apresentar(self):
        return f"{self.nome} é funcionário e recebe R$ {self.salario:.2f}"


class Gerente(Funcionario):
    def __init__(self, nome, salario=0, departamento="") -> None:
        super().__init__(nome, salario)
        self.departamento = departamento

    def apresentar(self):
        return f"{self.nome} é gerente de {self.departamento} e recebe R$ {self.salario:.2f}"


class Vendedor(Funcionario):
    def __init__(self, nome, salario=0, comissao=0) -> None:
        super().__init__(nome, salario)
        self.comissao = comissao

    def calcular_remuneracao(self):
        return self.salario + self.comissao

    def apresentar(self):
        return f"{self.nome} é vendedor e ganha salário de R$ {self.salario:.2f}, comissão de R$ {self.comissao:.2f} e remuneração total de R$ {self.calcular_remuneracao():.2f}"


if __name__ == "__main__":
    funcionarios = [
        Funcionario("Ana", 2500),
        Gerente("Carlos", 6500, "Tecnologia"),
        Vendedor("Marcos", 2200, 500)
    ]

    for funcionario in funcionarios:
        print(funcionario.apresentar())
