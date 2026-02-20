from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypeAlias

Number: TypeAlias = int | float


class Calculo(ABC):
    @abstractmethod
    def calcular(self, n1: Number, n2: Number) -> Number:
        raise NotImplementedError


class Soma(Calculo):
    def calcular(self, n1: Number, n2: Number) -> Number:
        return n1 + n2


class Subtracao(Calculo):
    def calcular(self, n1: Number, n2: Number) -> Number:
        return n1 - n2


class Multiplicacao(Calculo):
    def calcular(self, n1: Number, n2: Number) -> Number:
        return n1 * n2


class Divisao(Calculo):
    def calcular(self, n1: Number, n2: Number) -> Number:
        self.check_divisor(n2)
        return n1 / n2

    @staticmethod
    def check_divisor(n2: Number) -> None:
        if n2 == 0:
            raise ZeroDivisionError("Erro de divisão por 0")


OPTIONS: dict[str, type[Calculo]] = {
    "+": Soma,
    "-": Subtracao,
    "/": Divisao,
    "*": Multiplicacao,
}


class Calculadora:
    @classmethod
    def get_operacao(cls, operador: str) -> Calculo:
        operacao_cls = OPTIONS.get(operador)
        if operacao_cls is None:
            raise ValueError(f"Operador {operador} não encontrado!")
        return operacao_cls()


if __name__ == "__main__":
    while True:
        try:
            n1 = float(input("N1: ").replace(",", "."))
            n2 = float(input("N2: ").replace(",", "."))
        except ValueError:
            print("Digite apenas números...")
            continue

        opc = input("Operador [+, -, *, /, !(Sair)]: ")
        if opc == "!":
            break

        try:
            c = Calculadora.get_operacao(opc)
            resultado = c.calcular(n1, n2)
        except (ValueError, ZeroDivisionError) as e:
            print(e)
            continue

        print("==" * 30)
        print(f"{n1} {opc} {n2} = {resultado}")
        print("==" * 30)
