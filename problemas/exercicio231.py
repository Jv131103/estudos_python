from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome="", salario_base=0) -> None:
        self.nome = nome
        self.salario_base = salario_base

    @abstractmethod
    def salario_final(self):
        return self.salario_base

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(nome={self.nome}, salario={self.salario_base:.2f})"


class Gerente(Funcionario):
    def __init__(self, nome, salario_base) -> None:
        super().__init__(nome, salario_base)

    def salario_final(self):
        return 2000 + self.salario_base


class Estagiario(Funcionario):
    def __init__(self, nome, salario_base) -> None:
        super().__init__(nome, salario_base)

    def salario_final(self):
        return self.salario_base * 0.8


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, percentual) -> None:
        super().__init__(nome, salario_base)
        self.percentual = percentual

    def salario_final(self):
        return self.salario_base + (self.salario_base * self.percentual / 100)


f1 = Gerente("Renato", 5000)
print(f1)
print(f1.salario_final())  # 7000

f2 = Estagiario("João", 2000)
print(f2)
print(f2.salario_final())  # 1600

f3 = Vendedor("Carlos", 3000, 10)
print(f3)
print(f3.salario_final())  # 3300
