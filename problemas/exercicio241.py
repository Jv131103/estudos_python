class FilaDePrioridade:
    def __init__(self) -> None:
        self.fila = []

    def enfileirar(self, valor, prioridade):
        if not self.fila:
            self.fila.append((valor, prioridade))
            return

        pos = 0
        for dados in self.fila:
            prioridade_inserida = dados[1]
            if prioridade > prioridade_inserida:
                self.fila.insert(pos, (valor, prioridade))
                return  # <<< para aqui (inseriu 1 vez)
            pos += 1

        # se não inseriu em nenhum lugar, vai pro final
        self.fila.append((valor, prioridade))

    def desenfileirar(self):
        if not self.fila:
            print("Fila vazia")
            return None
        return self.fila.pop(0)

    def exibir(self):
        for dados in self.fila:
            print(f"{dados[0]}({dados[1]}) -> ", end="")
        print("None")


f = FilaDePrioridade()
f.enfileirar("A", 1)
f.enfileirar("B", 3)
f.enfileirar("C", 2)

f.exibir()                 # B(3) -> C(2) -> A(1) -> None
print(f.desenfileirar())   # ('B', 3)
