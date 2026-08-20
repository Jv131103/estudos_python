class Dinheiro:
    def __init__(self, valor, moeda) -> None:
        self.valor = valor
        self.moeda = moeda

    def __str__(self) -> str:
        return f"{self.moeda} {self.valor:.2f}"

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Dinheiro):
            return self.valor == value.valor and self.moeda == value.moeda
        return False

    def __add__(self, other):
        if isinstance(other, Dinheiro):
            if other.moeda == self.moeda:
                return Dinheiro(self.valor + other.valor, self.moeda)
            raise ValueError("MOEDAS DIFERENTES!")
        return NotImplemented


a = Dinheiro(100, "BRL")
b = Dinheiro(50, "BRL")
c = Dinheiro(30, "USD")

print(a + b)       # BRL = 150.00
print(a == Dinheiro(100, "BRL"))  # True
print(a + c)       # deve levantar exceção (moedas diferentes)
