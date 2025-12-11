class Calculadora:
    def __init__(self) -> None:
        self.logs = []

    def somar(self, a, b):
        soma = a + b
        self.logs.append(["SOMA", f"{a} + {b} = {soma}"])
        return soma

    def subtrair(self, a, b):
        subtracao = a - b
        self.logs.append(["SUBTRACAO", f"{a} - {b} = {subtracao}"])
        return subtracao

    def multiplicar(self, a, b):
        multiplicacao = a * b
        self.logs.append(["MULTIPLICACAO", f"{a} x {b} = {multiplicacao}"])
        return multiplicacao

    def dividir(self, a, b):
        if b == 0:
            divisao = None
            self.logs.append(["DIVISAO (ERRO DE DIVISÃO POR 0)", f"{a} / {b} = {divisao}"])
            return
        divisao = a / b
        self.logs.append(["DIVISAO", f"{a} / {b} = {divisao}"])
        return divisao

    def historico(self):
        for log in self.logs:
            print("--" * 30)
            print(log)
            print("--" * 30)


c = Calculadora()
c.somar(3, 5)
c.dividir(10, 2)
c.historico()
