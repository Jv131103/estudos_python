import pytest
from src.main import inverter_com_classe, inverter_lista_direto


@pytest.mark.parametrize(
    "string,inverso",
    [
        ("Python", "nohtyP"),
        ("arara", "arara"),
        ("teste", "etset"),
        ("BDD", "DDB"),
        ("Arroz", "zorrA"),
        ("123", "321"),
        ("Olá Mundo!", "!odnuM álO"),
        ("Leão", "oãeL"),
        ("4002-8922", "2298-2004")
    ]
)
class TestInverterStrigComFila:
    def test_inverter_com_fila_modelo_classe(self, string, inverso):
        assert inverter_com_classe(string) == inverso

    def test_inverter_com_fila_modelo_lista_direto(self, string, inverso):
        assert inverter_lista_direto(string) == inverso
