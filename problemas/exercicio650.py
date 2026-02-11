"""
Crie uma classe Pedido com classe aninhada Status contendo constantes.
"""

from enum import Enum


class Pedido:
    class Status(Enum):
        PAGO = "PAGO"
        EM_ANDAMENTO = "EM_ANDAMENTO"
        EM_ABERTO = "EM_ABERTO"

    def __init__(self, status: Status) -> None:
        self.status = status

    def retornar_status(self):
        match self.status:
            case Pedido.Status.PAGO:
                print("Pronto para entrega")
            case Pedido.Status.EM_ANDAMENTO:
                print("Pedido em andamento no pagamento")
            case Pedido.Status.EM_ABERTO:
                print("Ainda a pagar")


pedido_n12345 = Pedido(Pedido.Status.PAGO)
pedido_n12345.retornar_status()
