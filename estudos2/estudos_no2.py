class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.prox = None
        self.ant = None


class ListaEncadeada:
    def __init__(self) -> None:
        self.inicio = None
        self.fim = None

    def inserir(self, valor):
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            return
        # Com self.fim não precisa de while — O(1)
        novo.ant = self.fim
        self.fim.prox = novo
        self.fim = novo  # ← atualiza o fim

    def inserir_inicio(self, valor):
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
            return
        novo.prox = self.inicio  # novo aponta para o antigo início
        self.inicio.ant = novo   # antigo início aponta de volta
        self.inicio = novo       # atualiza o início

    def contar_nos(self):
        cont = 0

        dados = self.inicio
        while dados:
            cont += 1
            dados = dados.prox

        return cont

    def ultimo_valor(self):
        dados = self.inicio
        while dados:
            valor = dados.valor
            dados = dados.prox

        return valor

    def __str__(self) -> str:
        uniao = ""
        dados = self.inicio
        while dados:
            uniao += f"{dados.valor}"
            if dados.prox:
                uniao += " <-> "
            dados = dados.prox
        return uniao

    def __str_reverso__(self) -> str:
        uniao = ""
        dados = self.fim  # começa do fim
        while dados:
            uniao += f"{dados.valor}"
            if dados.ant:
                uniao += " <-> "
            dados = dados.ant  # anda para trás
        return uniao


li = ListaEncadeada()
li.inserir(1)
li.inserir(2)
li.inserir(3)
li.inserir_inicio(4)
li.inserir_inicio(5)
li.inserir_inicio(6)
print(li)
print(li.contar_nos())
print(li.ultimo_valor())
