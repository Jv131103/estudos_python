"""
Leia uma linha no formato:

    Produto=Notebook;Preco=3.499,90;Qtd=2


Mostre:

    nome do produto

    preço como float

    quantidade como int

    valor total (preço * quantidade)

Dicas:

    split(";")

    depois split("=")

    tratar vírgula decimal
"""


def mostrar_produto(texto):
    dados = texto.split(";")
    if len(dados) != 3:
        print("Formato inválido!")
        print("Formato ideal EX: Produto=Notebook;Preco=3.499,90;Qtd=2")
        return

    valor_final = 1
    for dado in dados:
        if "=" not in dado:
            print("Formato inválido!")
            print("Formato ideal EX: [informacao]=[dado]")
            return
        info, valor = dado.split("=")

        if not valor.isalpha():
            valor = valor.replace(".", "").replace(",", ".")
            if valor.isdigit():
                valor = int(valor)
            else:
                valor = float(valor)
            valor_final *= valor

        print(f"{info}: {valor}")

    print(f"Valor total: {valor_final:.2f}")


mostrar_produto("Produto=Notebook;Preco=3.499,90;Qtd=2")
mostrar_produto("Produto=Notebook;Preco=3.499,90;Qtd=12")
