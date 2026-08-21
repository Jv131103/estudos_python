class No:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.esquerda = None
        self.direita = None


def na_mao():
    raiz = No(10)
    print(raiz.valor, raiz.esquerda, raiz.direita)

    raiz.esquerda = No(5)
    print(raiz.valor, raiz.esquerda, raiz.direita)

    raiz.esquerda.direita = No(7)
    print(raiz.valor, raiz.esquerda.valor, raiz.direita)
    print(raiz.valor, raiz.esquerda.direita.valor, raiz.direita)


def inserir_iterativo(raiz, valor):
    if raiz is None:
        print(f"Árvore vazia -> {valor} vira a raiz")
        return No(valor)

    atual = raiz
    print(f"Começando na raiz (valor={atual.valor}), tentando inserir {valor}")

    while True:
        if valor < atual.valor:
            print(f"{valor} < {atual.valor} -> vai pra ESQUERDA de {atual.valor}")
            if atual.esquerda is None:
                atual.esquerda = No(valor)
                print(f"  Esquerda de {atual.valor} tava vazia -> {valor} encaixado aqui!")
                return raiz
            else:
                print(f"  Esquerda de {atual.valor} já tem o nó {atual.esquerda.valor} -> descendo")
                atual = atual.esquerda
        else:
            print(f"{valor} >= {atual.valor} -> vai pra DIREITA de {atual.valor}")
            if atual.direita is None:
                atual.direita = No(valor)
                print(f"  Direita de {atual.valor} tava vazia -> {valor} encaixado aqui!")
                return raiz
            else:
                print(f"  Direita de {atual.valor} já tem o nó {atual.direita.valor} -> descendo")
                atual = atual.direita


raiz = None
for v in [10, 5, 7, 3, 12, 4, 0, 1, 2, 11]:
    raiz = inserir_iterativo(raiz, v)
    print("---")
