import pytest
from src.main import RingBuffer


def test_adicionar_um_log():
    rb = RingBuffer(4)

    rb.adicionar("A")

    assert rb.get_logs() == ["A"]


def test_adicionar_varios_logs():
    rb = RingBuffer(4)

    rb.adicionar("A")
    rb.adicionar("B")
    rb.adicionar("C")

    assert rb.get_logs() == ["A", "B", "C"]


def test_is_full_false_quando_nao_encheu():
    rb = RingBuffer(4)

    rb.adicionar("A")
    rb.adicionar("B")

    assert rb.is_full() is False


def test_is_full_true_quando_enche():
    rb = RingBuffer(4)

    rb.adicionar("A")
    rb.adicionar("B")
    rb.adicionar("C")
    rb.adicionar("D")

    assert rb.is_full() is True


def test_ring_buffer_sobrescreve_logs_antigos():
    rb = RingBuffer(4)

    rb.adicionar("A")
    rb.adicionar("B")
    rb.adicionar("C")
    rb.adicionar("D")
    rb.adicionar("E")
    rb.adicionar("F")

    assert rb.get_logs() == ["C", "D", "E", "F"]


def test_snapshot_salva_estado_atual():
    rb = RingBuffer(4)

    rb.adicionar("A")
    rb.adicionar("B")
    rb.adicionar("C")
    rb.adicionar("D")

    rb.snapshot()

    assert rb.get_snapshots() == [["A", "B", "C", "D"]]


def test_snapshot_salva_estados_diferentes():
    rb = RingBuffer(4)

    rb.adicionar("A")
    rb.adicionar("B")
    rb.adicionar("C")
    rb.adicionar("D")
    rb.snapshot()

    rb.adicionar("E")
    rb.adicionar("F")
    rb.snapshot()

    assert rb.get_snapshots() == [
        ["A", "B", "C", "D"],
        ["C", "D", "E", "F"]
    ]


def test_get_logs_nao_altera_snapshots():
    rb = RingBuffer(4)

    rb.adicionar("A")
    rb.adicionar("B")
    rb.adicionar("C")
    rb.adicionar("D")

    rb.get_logs()
    rb.get_logs()

    assert rb.get_snapshots() == []


def test_get_snapshots_inicia_vazio():
    rb = RingBuffer(4)

    assert rb.get_snapshots() == []


def test_buffer_capacidade_um():
    rb = RingBuffer(1)

    rb.adicionar("A")
    assert rb.get_logs() == ["A"]

    rb.adicionar("B")
    assert rb.get_logs() == ["B"]


@pytest.mark.parametrize(
    "entradas, esperado",
    [
        (["A"], ["A"]),
        (["A", "B"], ["A", "B"]),
        (["A", "B", "C", "D"], ["A", "B", "C", "D"]),
        (["A", "B", "C", "D", "E"], ["B", "C", "D", "E"]),
        (["A", "B", "C", "D", "E", "F"], ["C", "D", "E", "F"]),
    ],
)
def test_get_logs_varios_casos(entradas, esperado):
    rb = RingBuffer(4)

    for item in entradas:
        rb.adicionar(item)

    assert rb.get_logs() == esperado
