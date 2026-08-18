class ErrorEstoque(Exception):
    pass


class EstoqueInsuficienteError(ErrorEstoque):
    pass


class EstoqueVazioError(ErrorEstoque):
    pass


def comprar(estoque, produto, quantidade):
    if not isinstance(estoque, dict):
        print("Modelo inválido para simulação")
        raise TypeError("Tipo inválido para simulação de estoque")

    if not estoque:
        print("Não há estoque registrado")
        raise EstoqueVazioError("Sem estoque definido")

    if not isinstance(produto, str):
        print("Produto precisa ser do tipo str")
        raise ValueError("Tipo inválido para produto")

    if not isinstance(quantidade, (int, float)):
        print("Quantidade precisa ser do tipo int / float")
        raise ValueError("Tipo inválido para quantidade")

    if produto not in estoque:
        print("Produto não existe")
        raise KeyError(f"Produto '{produto}' não existe no estoque")

    total = estoque.get(produto, 0)
    print(f"Total em estoque de {produto}: {total}")
    if quantidade > total:
        print("estoque insuficiente")
        raise EstoqueInsuficienteError("Estoque insuficiente, compra negada!")


    total -= quantidade
    estoque[produto] = total

    print(f"Total em estoque de {produto} pós compra: {total}")
    print("Sucesso!")
    return estoque


estoque = {"maçã": 10, "banana": 0, "laranja": 5}
estoque = comprar(estoque, "maçã", 5)
estoque = comprar(estoque, "batata", 5)
