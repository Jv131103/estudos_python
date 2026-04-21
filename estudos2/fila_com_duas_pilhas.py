class FilaComDuasPilhas:
    def __init__(self) -> None:
        self.entrada = []
        self.saida = []

    def empty(self):
        return not self.entrada and not self.saida

    def enqueue(self, valor):
        self.entrada.append(valor)

    def __transferir_se_preciso(self):
        if not self.saida:
            while self.entrada:
                self.saida.append(self.entrada.pop())

    def dequeue(self):
        if self.empty():
            raise IndexError('Fila vazia!')

        self.__transferir_se_preciso()
        return self.saida.pop()

    def peek(self):
        if self.empty():
            raise IndexError('Fila vazia!')

        self.__transferir_se_preciso()
        return self.saida[-1]

    def __len__(self):
        return len(self.entrada) + len(self.saida)

    def __repr__(self):
        frente = list(reversed(self.saida)) + self.entrada
        return f"Fila(frente->{frente})"


fila = FilaComDuasPilhas()
print(fila)
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
print(fila)
print(fila.dequeue())
print(fila.peek())
print(fila)
fila.enqueue(40)
print(fila)
print(fila.dequeue())
print(fila.dequeue())
fila.enqueue(50)
print(fila.dequeue())
print(fila)
