class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.prox = None


class ListaEncadeada:
    def __init__(self) -> None:
        self.topo = None

    def inserir(self, valor):
        novo = No(valor)

        if self.topo is None:
            self.topo = novo
            return

        dado = self.topo

        while dado:
            if dado.prox is None:
                dado.prox = novo
                break
            dado = dado.prox

    def contar_nos(self):
        cont = 0

        dados = self.topo
        while dados:
            cont += 1
            dados = dados.prox

        return cont

    def ultimo_valor(self):
        dados = self.topo
        while dados:
            valor = dados.valor
            dados = dados.prox

        return valor

    def __str__(self) -> str:
        uniao = ""

        dados = self.topo
        while dados:
            uniao += f"{dados.valor} -> "
            dados = dados.prox

        uniao += "None"
        return uniao


li = ListaEncadeada()
li.inserir(1)
li.inserir(2)
li.inserir(3)
print(li)
print(li.contar_nos())
print(li.ultimo_valor())
