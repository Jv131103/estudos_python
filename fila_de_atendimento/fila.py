class Fila:
    def __init__(self) -> None:
        self._fila = []

    def is_empty(self):
        return len(self._fila) == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Fila Vazia!")
        return self._fila[0]

    def enqueue(self, valor):
        self._fila.append(valor)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Fila vazia!")

        return self._fila.pop(0)  # O(n)

    def listar(self):
        if self.is_empty():
            raise IndexError("Lista Vazia!")

        for pos, dados in enumerate(self._fila, start=1):
            saida = f"{pos} - {dados}"
            if pos == 1:
                saida += " Próximo"
            elif pos == len(self._fila):
                saida += " Último"

            print(saida)

    def __len__(self):
        return len(self._fila)

    def __str__(self):
        if self.is_empty():
            return "Fila([], status='Empty')"
        return f"Fila({self._fila}, primeiro={self._fila[0]}, ultimo={self._fila[-1]})"


if __name__ == "__main__":
    f = Fila()
    f.enqueue("A")
    f.enqueue("B")
    f.enqueue("C")
    print(f)
    print("Saiu:", f.dequeue())
    print(f)
    f.enqueue("D")
    f.enqueue("E")
    f.enqueue("F")
    f.enqueue("G")
    print("Saiu:", f.dequeue())
    f.listar()
