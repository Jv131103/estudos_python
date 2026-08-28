class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.proximo = None
        self.anterior = None  # Necessário para voltar do fim para o início


class Caixa:
    def __init__(self) -> None:
        self.inicio = None
        self.fim = None

    def inserir(self, valor):
        novo = No(valor)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.anterior = self.fim  # Aponta para o nó antigo do fim
            self.fim.proximo = novo   # Conecta o nó antigo ao novo
            self.fim = novo           # Atualiza o fim para o novo nó

    def existe(self, valor):
        esq = self.inicio
        dir = self.fim

        # Percorre enquanto os ponteiros não se cruzarem ou se sobreporem
        while esq and dir and esq != dir and esq.anterior != dir:
            if esq.valor == valor or dir.valor == valor:
                return True

            esq = esq.proximo     # Avança do início para o fim
            dir = dir.anterior    # Volta do fim para o início

        # Checagem final para quando esq e dir se encontrarem no mesmo nó
        if esq and esq.valor == valor:
            return True

        return False

    def ultima_caixa(self):
        if not self.fim:
            return None
        return self.fim.valor  # Acesso direto sem precisar de loop


c = Caixa()
c.inserir(10)
c.inserir(20)
c.inserir(30)
c.inserir(40)

print(c.existe(30))
print(c.existe(99))

ultima = c.ultima_caixa()
print(ultima)  # 40
