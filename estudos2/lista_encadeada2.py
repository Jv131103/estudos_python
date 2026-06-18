class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self) -> None:
        self.cabeca = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.cabeca
        self.cabeca = novo

    def inserir_final(self, valor):
        novo = No(valor)
        if self.cabeca is None:
            self.cabeca = novo
            return

        dado = self.cabeca
        while dado.proximo:
            dado = dado.proximo

        dado.proximo = novo

    def remover(self, valor):
        if not self.cabeca:
            return None

        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            return

        anterior = self.cabeca
        atual = self.cabeca.proximo

        while atual:
            if atual.valor == valor:
                anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo

        print(f"Valor {valor} não encontrado!")

    def inverter(self):
        troca = None
        dado = self.cabeca
        while dado:
            proximo_cabeca = dado.proximo
            dado.proximo = troca

            troca = dado
            dado = proximo_cabeca

        self.cabeca = troca

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def __str__(self) -> str:
        uniao = ""

        cabeca = self.cabeca
        while cabeca:
            uniao += f"{cabeca.valor} -> "
            cabeca = cabeca.proximo

        uniao += "None"
        return uniao


li = ListaEncadeada()

li.inserir_inicio(1)
li.inserir_inicio(2)
li.inserir_final(3)
li.inserir_final(4)
print(li)
li.remover(3)
print(li)
li.inverter()
print(li)
li.inverter()
print(li)
