class Pilha:

    def __init__(self):
        self.dados = []

    def push(self, valor):
        self.dados.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.dados.pop()

    def peek(self):
        if not self.is_empty():
            return self.dados[-1]

    def is_empty(self):
        return len(self.dados) == 0


def inverter_com_classe(string):
    inverso = []

    p = Pilha()

    for char in string:
        p.push(char)

    while not p.is_empty():
        inverso.append(p.pop())

    return "".join(inverso)


def inverter_lista_direto(string):
    inverso = []

    pilha = []

    for char in string:
        pilha.append(char)

    while pilha:
        inverso.append(pilha.pop())

    return "".join(inverso)


if __name__ == "__main__":
    print(inverter_com_classe("python"))
    print(inverter_lista_direto("python"))
