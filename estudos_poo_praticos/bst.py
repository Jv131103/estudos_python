class No:
    def __init__(self, valor) -> None:
        self.esquerda = None
        self.direita = None
        self.valor = valor


class ArvoreBinaria:
    def __init__(self) -> None:
        self.head = None

    def inserir(self, valor):
        self.head = self._inserir_recursivo(self.head, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if no_atual is None:
            return No(valor)

        if valor < no_atual.valor:
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, valor)
        else:
            no_atual.direita = self._inserir_recursivo(no_atual.direita, valor)

        return no_atual

    def buscar(self, valor):
        return self._buscar_recursivo(self.head, valor)

    def _buscar_recursivo(self, no_atual, valor):
        if no_atual is None:
            return False

        if no_atual.valor == valor:
            return True

        if valor < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerda, valor)
        else:
            return self._buscar_recursivo(no_atual.direita, valor)

    def em_ordem(self):
        return self._ordem_recursivo(self.head, [])

    def _ordem_recursivo(self, no_atual, lista_resultado):
        if no_atual is None:
            return lista_resultado

        self._ordem_recursivo(no_atual.esquerda, lista_resultado)
        lista_resultado.append(no_atual.valor)
        self._ordem_recursivo(no_atual.direita, lista_resultado)

        return lista_resultado


arvore = ArvoreBinaria()
for v in [50, 30, 70, 20, 40, 60, 80]:
    arvore.inserir(v)

print(arvore.em_ordem())
