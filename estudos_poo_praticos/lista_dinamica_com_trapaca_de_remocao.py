class ArrayDinamico:
    def __init__(self):
        self.capacidade = 2
        self.tamanho = 0
        self.inicio = 0  # inicio → aponta pro primeiro elemento. Circulariza o array
        self.dados = [None] * self.capacidade

    def adicionar(self, valor):
        if self.tamanho == self.capacidade:
            self._redimensionar()

        # calcula posição real (circular)
        pos = (self.inicio + self.tamanho) % self.capacidade
        self.dados[pos] = valor
        self.tamanho += 1

    def obter(self, indice):
        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice fora do limite")

        # converte índice lógico → físico
        pos = (self.inicio + indice) % self.capacidade
        return self.dados[pos]

    def definir(self, indice, valor):
        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice fora do limite")

        pos = (self.inicio + indice) % self.capacidade
        self.dados[pos] = valor

    def deletar(self, indice=None):
        if indice is None:
            indice = self.tamanho - 1

        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice fora do limite")

        # 🔥 CASO ESPECIAL: deletar primeiro → O(1)
        if indice == 0:
            self.dados[self.inicio] = None
            self.inicio = (self.inicio + 1) % self.capacidade
            self.tamanho -= 1
            return

        # 🔥 CASO GERAL: continua O(n)
        for i in range(indice, self.tamanho - 1):
            atual = (self.inicio + i) % self.capacidade
            prox = (self.inicio + i + 1) % self.capacidade
            self.dados[atual] = self.dados[prox]

        # limpa último
        ultimo = (self.inicio + self.tamanho - 1) % self.capacidade
        self.dados[ultimo] = None

        self.tamanho -= 1

    def _redimensionar(self):
        nova_capacidade = self.capacidade * 2
        novo = [None] * nova_capacidade

        # copia respeitando ordem lógica
        for i in range(self.tamanho):
            pos = (self.inicio + i) % self.capacidade
            novo[i] = self.dados[pos]

        self.dados = novo
        self.capacidade = nova_capacidade
        self.inicio = 0  # reseta

    def __str__(self):
        elementos = []
        for i in range(self.tamanho):
            pos = (self.inicio + i) % self.capacidade
            elementos.append(self.dados[pos])
        return str(elementos)


arr = ArrayDinamico()

arr.adicionar(10)
arr.adicionar(20)
arr.adicionar(30)  # aqui vai redimensionar
arr.adicionar(40)
arr.adicionar(50)
arr.adicionar(60)  # aqui vai redimensionar

print(arr)

arr.deletar()
arr.deletar(2)
arr.deletar(0)
print(arr)
