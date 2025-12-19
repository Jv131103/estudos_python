class FilaSimples:
    def __init__(self) -> None:
        self.fila = []

    def vazia(self):
        return len(self.fila) == 0

    def entrar(self, valor):
        self.fila.append(valor)

    def sair(self):
        if not self.vazia():
            return self.fila.pop(0)

    def saida(self):
        for i in range(len(self.fila) - 1):
            print(f"{self.fila[i]} <-- ", end="")
        print(f"{self.fila[-1]}")


f = FilaSimples()
print(f.vazia())
f.entrar('a')
f.entrar('b')
f.entrar('c')
f.entrar('d')
f.saida()
f.sair()
f.sair()
f.saida()
