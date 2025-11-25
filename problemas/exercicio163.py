class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def n2_is_0(self):
        if self.n2 == 0:
            raise ZeroDivisionError("Erro de divisão por 0")

    def soma(self):
        return self.n1 + self.n2

    def subtracao(self):
        return self.n1 - self.n2

    def multiplicacao(self):
        return self.n1 * self.n2

    def divisao(self):
        self.n2_is_0()
        return self.n1 / self.n2

    def divisao_inteiro(self):
        self.n2_is_0()
        return self.n1 // self.n2

    def divisao_modulo(self):
        self.n2_is_0()
        return self.n1 % self.n2

    def potencia(self):
        return self.n1**self.n2

    def raiz(self):
        return self.n1**(1 / self.n2)

    def percent(self):
        return self.n1 * (self.n2 / 100)

    def part_percent(self):
        return (self.n1 / self.n2) * 100

    def retornar_todos(self):
        retornos = [
            (self.soma, '+'),
            (self.subtracao, '-'),
            (self.multiplicacao, 'x'),
            (self.divisao, '÷'),
            (self.divisao_inteiro, '÷(int)'),
            (self.divisao_modulo, '÷(mod)'),
            (self.potencia, "**"),
            (self.raiz, '√'),
            (self.percent, "%"),
            (self.part_percent, "%(part)"),
        ]

        print("==" * 30)
        print("\t\tRESULTADOS DA CALCULADORA\n" + "==" * 30)
        for retorno in retornos:
            calculo, value = retorno
            if value == '√':
                print(f"{self.n2}{value}{self.n1} = {calculo()}")
            else:
                print(f"{self.n1} {value} {self.n2} = {calculo()}")
            print("--" * 30)


c = Calculadora(2, 2)
c.retornar_todos()
