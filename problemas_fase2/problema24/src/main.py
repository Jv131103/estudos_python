class Fila:

    def __init__(self):
        self.dados = []

    def enqueue(self, valor):
        self.dados.append(valor)

    def dequeue(self):
        if not self.is_empty():
            return self.dados.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.dados[0]

    def is_empty(self):
        return len(self.dados) == 0


def gerar_binarios_fila(n):
    fila = Fila()
    fila.enqueue("1")
    resultado = []

    for _ in range(n):
        atual = fila.dequeue()
        resultado.append(atual)

        fila.enqueue(atual + "0")
        fila.enqueue(atual + "1")

    return resultado


def gerar_binario_fila_lista_direta(n):
    fila = ["1"]
    resultado = []

    for _ in range(n):
        atual = fila.pop(0)
        resultado.append(atual)

        fila.append(atual + "0")
        fila.append(atual + "1")

    return resultado


def gerar_binarios_manual(n):
    resultado = []

    for numero in range(1, n + 1):
        num = numero
        lista = []

        while num != 0:
            lista.append(str(num % 2))
            num //= 2

        resultado.append("".join(lista[::-1]))

    return resultado


def gerar_binarios_bin(n):
    resultado = []

    for num in range(1, n + 1):
        resultado.append(bin(num)[2:])

    return resultado


def gerar_binarios_fstring(n):
    resultado = []

    for num in range(1, n + 1):
        resultado.append(f"{num:b}")

    return resultado


def decimal_para_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_para_binario(n // 2) + str(n % 2)


def gerar_binarios_recursivo(n):
    resultado = []

    for num in range(1, n + 1):
        resultado.append(decimal_para_binario(num))

    return resultado


if __name__ == "__main__":
    print(gerar_binarios_fila(5))
    print()
    print(gerar_binario_fila_lista_direta(5))
    print()
    print(gerar_binarios_manual(5))
    print()
    print(gerar_binarios_bin(5))
    print()
    print(gerar_binarios_fstring(5))
    print()
    print(gerar_binarios_recursivo(5))
