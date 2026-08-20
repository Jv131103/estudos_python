class Contador:
    def __init__(self, inicio, fim) -> None:
        self.atual = inicio
        self.fim = fim
        self.passo = 1 if inicio <= fim else -1

    def __iter__(self):
        return self

    def __next__(self):
        if (self.passo == 1 and self.atual > self.fim) or (self.passo == -1 and self.atual < self.fim):
            raise StopIteration

        resultado = self.atual
        self.atual += self.passo
        return resultado


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
