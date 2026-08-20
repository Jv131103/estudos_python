class Contador:
    def __init__(self, inicio, fim) -> None:
        self.inicio = inicio
        self.fim = fim
        if inicio > fim:
            self.crescente = False
        else:
            self.crescente = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.inicio <= self.fim and self.crescente:
            resultado = self.inicio
            self.inicio += 1
            return resultado
        elif self.inicio >= self.fim and not self.crescente:
            resultado = self.inicio
            self.inicio -= 1
            return resultado
        raise StopIteration


c = Contador(1, 5)
for numero in c:
    print(numero)

print()

c = Contador(5, 1)
for numero in c:
    print(numero)

print()

c = Contador(1, 1)
for numero in c:
    print(numero)
