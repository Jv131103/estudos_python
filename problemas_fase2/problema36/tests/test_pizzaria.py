import pytest
from src.pizzaria import Bebida, Pedido, Pizza  # seu arquivo anterior


class TestPizza:
    def test_preco_tamanho_g(self):
        pizza_tamanho_g = Pizza("G", ["Teste", "Teste"])
        assert pizza_tamanho_g.preco == 45

    def test_tamanho_invalido(self):
        with pytest.raises(ValueError):
            Pizza("A", ["erro"])

    def test_adicionar_sabor(self):
        pizza_peperoni = Pizza("M", ["peperoni"])
        pizza_peperoni.adicionar_sabor("Anchovas")
        assert len(pizza_peperoni.sabores) == 2

    def test_limite_sabores(self):
        pizza_peperoni = Pizza("M", ["peperoni"])
        pizza_peperoni.adicionar_sabor("Anchovas")
        assert pizza_peperoni.adicionar_sabor("Molho Tártaro") is None

    def test_descricao_sem_sabor(self):
        pizza = Pizza("M")
        assert pizza.descricao() == "Nenhum sabor pedido!"


class TestBebida:
    def test_nome_com_volume(self):
        coca_cola = Bebida("Coca-Cola", 6, "350ml")
        assert coca_cola.nome == "Coca-Cola 350ml"

    def test_descricao(self):
        coca_cola = Bebida("Coca-Cola", 6, "350ml")
        assert coca_cola.descricao() == "🥤 Coca-Cola 350ml - R$ 6.00"


class TestPedido:
    def test_adicionar_item(self):
        pizza_calabreza = Pizza("M", ["Calabresa"])
        coca_cola = Bebida("Coca-Cola", 6, "350ml")
        pedido = Pedido("João")
        pedido.adicionar_item(pizza_calabreza)
        pedido.adicionar_item(coca_cola)
        assert len(pedido.itens) == 2

    def test_total(self):
        pizza_calabreza = Pizza("M", ["Calabresa"])
        coca_cola = Bebida("Coca-Cola", 6, "350ml")
        pedido = Pedido("João")
        pedido.adicionar_item(pizza_calabreza)
        pedido.adicionar_item(coca_cola)
        assert pedido.total() == "Total: R$ 41.00"
