class Fila:
    def __init__(self) -> None:
        self.fila = []

    def enfileirar(self, valor):
        self.fila.append(valor)

    def desenfileirar(self):
        if self.vazia():
            print("Pilha Vazia")
            return
        return self.fila.pop(0)

    def primeiro(self):
        if self.vazia():
            print("Pilha Vazia")
            return
        return self.fila[0]

    def vazia(self):
        return len(self.fila) == 0


f = Fila()
f.enfileirar("A")
f.enfileirar("B")
print(f.primeiro())
print(f.desenfileirar())
print(f.desenfileirar())
print(f.vazia())
