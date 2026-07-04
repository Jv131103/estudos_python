class Carta:
    def __init__(self, valor, naipe) -> None:
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor}{self.naipe}"

    def __repr__(self):
        return f"Carta({self.valor!r}, {self.naipe!r})"

    def __eq__(self, other):
        if not isinstance(other, Carta):
            return NotImplemented

        return (
            self.valor == other.valor
            and self.naipe == other.naipe
        )


class Mao:
    def __init__(self, cartas=None) -> None:
        self.cartas = cartas or []

    def __len__(self):
        return len(self.cartas)

    def __contains__(self, item):
        return item in self.cartas

    def __iter__(self):
        return iter(self.cartas)

    def __getitem__(self, indice):
        return self.cartas[indice]

    def __reversed__(self):
        return reversed(self.cartas)

    def __bool__(self):
        return len(self) > 0

    def __str__(self):
        return ", ".join(str(carta) for carta in self.cartas)

    def __repr__(self):
        return f"Mao({self.cartas!r})"


mao = Mao([
    Carta("A", "♠"),
    Carta("K", "♥"),
    Carta("Q", "♦")
])

print(mao)
print()

print(len(mao))
print()

print(Carta("A", "♠") in mao)
print(Carta("10", "♣") in mao)
print()

print(mao[1])
print()

for carta in mao:
    print(carta, end=" ")

print("\n")

for carta in reversed(mao):
    print(carta, end=" ")

print("\n")

if mao:
    print("A mão possui cartas.")
