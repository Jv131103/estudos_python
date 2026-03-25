class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.filho = None


class ArvoreUnaria:
    def __init__(self) -> None:
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)
        if not self.raiz:
            self.raiz = novo
            return

        atual = self.raiz

        while atual.filho is not None:
            atual = atual.filho

        atual.filho = novo

    def buscar(self, valor):
        current = self.raiz

        while current:
            if current.valor == valor:
                return True
            current = current.filho
        return False

    def contar_no(self):
        current = self.raiz

        cont = 0

        while current:
            cont += 1
            current = current.filho
        return cont

    def imprimir(self):
        current = self.raiz

        while current:
            print(current.valor)
            current = current.filho

    def inverter(self):
        prev = None
        current = self.raiz

        while current:
            proximo_node = current.filho
            current.filho = prev

            prev = current
            current = proximo_node

        self.raiz = prev
        return self.raiz


if __name__ == "__main__":
    arvore = ArvoreUnaria()
    arvore.inserir(10)
    arvore.inserir(20)
    arvore.inserir(30)
    arvore.inserir(40)
    arvore.imprimir()
    print(arvore.buscar(20))
    print(arvore.buscar(50))
    print(arvore.contar_no())
    arvore.inverter()
    arvore.imprimir()
