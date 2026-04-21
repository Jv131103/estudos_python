entrada = []
saida = []


def enqueue(valor):
    entrada.append(valor)


def transferir():  # O(n)
    if not saida:
        while entrada:
            saida.append(entrada.pop())


def dequeue():  # O(1) amortizado por que tranferir é O(n)
    if not entrada and not saida:
        raise IndexError("Fila Vazia")

    transferir()
    return saida.pop()


def peek():  # O(1) amortizado por que tranferir é O(n)
    if not entrada and not saida:
        raise IndexError("Fila Vazia")

    transferir()
    return saida[-1]


def ler():
    return list(reversed(saida)) + entrada


print(ler())
enqueue(10)
enqueue(20)
enqueue(30)
print(ler())
print(peek())
print(ler())
dequeue()
print(peek())
print(ler())
