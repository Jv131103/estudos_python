class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        print(self.valor)


class ListaEncadeadaExtremidadeDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro is None

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print('A lista está vazia')
            return
        temp = self.primeiro
        if self.primeiro.proximo is None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp


class FilaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeadaExtremidadeDupla()

    def fila_vazia(self):
        return self.lista.lista_vazia()

    def enfileirar(self, valor):
        self.lista.insere_final(valor)

    def desenfileirar(self):
        return self.lista.excluir_inicio()

    def ver_inicio(self):
        if self.lista.primeiro is None:
            return -1
        return self.lista.primeiro.valor


if __name__ == "__main__":
    fila = FilaListaEncadeada()

    fila.enfileirar(20)
    fila.enfileirar(40)

    fila.ver_inicio()

    fila.enfileirar(60)
    fila.enfileirar(80)

    print(fila.ver_inicio())

    print(fila.desenfileirar())
    print(fila.ver_inicio())

    print(fila.desenfileirar())
    print(fila.desenfileirar())
    print(fila.desenfileirar())
    print(fila.ver_inicio())
