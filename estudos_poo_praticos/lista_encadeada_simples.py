class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.proximo = None


class Caixa:
    def __init__(self) -> None:
        self.ponteiro = None

    # Percorrendo até o fim (sem alterar a estrutura da classe)
    def inserir(self, valor):
        novo = No(valor)

        # Se a lista estiver vazia, o novo nó vira o início
        if self.ponteiro is None:
            self.ponteiro = novo
            return

        # Percorre até o último nó existente
        atual = self.ponteiro
        while atual.proximo:
            atual = atual.proximo

        # Conecta o novo nó ao final
        atual.proximo = novo

    def qtd_caixas(self):
        cont = 0
        atual = self.ponteiro
        while atual:
            cont += 1
            atual = atual.proximo

        return cont

    def existe(self, valor):
        atual = self.ponteiro
        while atual:
            if valor == atual.valor:
                return True
            atual = atual.proximo

        return False

    def primeira_caixa(self):
        if not self.ponteiro:
            return None
        return self.ponteiro.valor

    def ultima_caixa(self):
        if not self.ponteiro:
            return None
        atual = self.ponteiro
        while atual.proximo:
            atual = atual.proximo
        return atual.valor


c = Caixa()
c.inserir(10)
c.inserir(20)
c.inserir(30)
c.inserir(40)

print(c.qtd_caixas())

print(c.existe(30))
print(c.existe(99))

ultima = c.ultima_caixa()
print(ultima)  # 40
