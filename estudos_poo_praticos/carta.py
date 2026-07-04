class Carta:
    def __init__(self, valor, naipe) -> None:
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor}{self.naipe}"

    def __repr__(self):
        return f"Carta({self.valor}, {self.naipe})"


class Mao:
    def __init__(self, cartas) -> None:
        self.cartas = cartas

    def __len__(self):
        return len(self.cartas)

    def __contains__(self, item):
        return item in self.cartas

    def __iter__(self):
        return iter(self.cartas)


carta = Carta("A", "♠")
print(carta)

mao = Mao([Carta("A", "♠"), Carta("K", "♥"), Carta("Q", "♦")])
print(len(mao))
print(Carta("A", "♠") in mao)
for carta in mao:
    print(carta, end=" ")
print()
