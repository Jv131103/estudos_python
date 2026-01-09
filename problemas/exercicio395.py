class PilhaDesfazer:
    def __init__(self) -> None:
        self.pilha = []  # guarda os textos adicionados

    def add(self, texto: str) -> None:
        self.pilha.append(texto)

    def undo(self) -> None:
        if self.pilha:
            self.pilha.pop()

    def show(self) -> str:
        return "".join(self.pilha)


pilha = PilhaDesfazer()
pilha.add("oi")
pilha.add("tudo")
print(pilha.show())
pilha.undo()
print(pilha.show())
pilha.undo()
print(pilha.show())
