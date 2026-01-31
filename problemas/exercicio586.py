"""
Faça uma função sacar(valor) que:

    Receba um valor numérico

    Lance (raise) uma exceção se:

        o valor for menor ou igual a zero

        Retorne o valor se for válido
"""


class SaldoInsuficiente(Exception):
    pass


def sacar(valor):
    if not isinstance(valor, (int, float)):
        raise TypeError("Valor precisa ser numérico")

    if valor <= 0:
        raise SaldoInsuficiente("Saldo insuficiente, precisa ser maior que 0")

    return valor


valores = [1000, -1000, "abc"]

for v in valores:
    try:
        print(sacar(v))
    except SaldoInsuficiente as e:
        print(e)
    except TypeError as e:
        print(e)
