class Contador:
    total = 0

    def __init__(self) -> None:
        Contador.total += 1


c1 = Contador()
c2 = Contador()
c3 = Contador()

print(Contador.total)
