class ArrayDinamico:
    def __init__(self):
        self.capacidade = 2
        self.tamanho = 0
        self.dados = [None] * self.capacidade

    def adicionar(self, valor):
        # Se os tamanho sobrepor a capacidade, redimensiona alocando mais espaços
        if self.tamanho == self.capacidade:
            self._redimensionar()

        # Adiciona o dado novo na lista alocada
        self.dados[self.tamanho] = valor

        # Incrementa o tamanho
        self.tamanho += 1

    def obter(self, indice):
        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice fora do limite")

        # retorna os dados
        return self.dados[indice]

    def definir(self, indice, valor):
        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice fora do limite")

        # Faz a substituição ou adição implícita
        self.dados[indice] = valor

    def deletar(self, indice=None):
        if indice is None:
            indice = self.tamanho - 1

        if indice < 0 or indice >= self.tamanho:
            raise IndexError("Índice fora do limite")

        # move os elementos para a esquerda
        for i in range(indice, self.tamanho - 1):
            self.dados[i] = self.dados[i + 1]

        # limpa o último espaço
        self.dados[self.tamanho - 1] = None

        # diminui o tamanho
        self.tamanho -= 1

    def _redimensionar(self):
        self.capacidade *= 2

        # Adiciona mais 2 espaços
        novo = [None] * self.capacidade

        # Percorre e tranforma e readiciona os dados nessa nova lista
        for i in range(self.tamanho):
            novo[i] = self.dados[i]

        # Converte o novo para os dados principal
        self.dados = novo

    def tamanho_total(self):
        return self.tamanho

    def ultimo_indice(self):
        if self.tamanho == 0:
            return None
        return self.tamanho - 1

    def __str__(self):
        return str(self.dados[:self.tamanho])


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
