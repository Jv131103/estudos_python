class Calculadora:
    def __init__(self):
        self.logs = []

    def _registrar(self, tipo, a, b, resultado):
        self.logs.append(f"{tipo}: {a} ? {b} = {resultado}")

    def somar(self, a, b):
        r = a + b
        self._registrar("SOMA", a, b, r)
        return r

    def subtrair(self, a, b):
        r = a - b
        self._registrar("SUBTRAÇÃO", a, b, r)
        return r

    def multiplicar(self, a, b):
        r = a * b
        self._registrar("MULTIPLICAÇÃO", a, b, r)
        return r

    def dividir(self, a, b):
        if b == 0:
            self._registrar("DIVISÃO (ERRO)", a, b, "NÃO PERMITIDA")
            return None
        r = a / b
        self._registrar("DIVISÃO", a, b, r)
        return r

    def historico(self):
        print("\nHISTÓRICO:")
        for item in self.logs:
            print("--", item)


c = Calculadora()
c.somar(3, 5)
c.dividir(10, 2)
c.historico()
