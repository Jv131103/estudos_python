from enum import Enum


class Status(Enum):
    PENDENTE = 1
    PAGO = 2
    ENVIADO = 3
    ENTREGUE = 4


def proximo_status(status):
    match status:
        case Status.PENDENTE:
            return Status.PAGO
        case Status.PAGO:
            return Status.ENVIADO
        case Status.ENVIADO:
            return Status.ENTREGUE
        case Status.ENTREGUE:
            return Status.ENTREGUE


status = Status.PENDENTE
print(status)
status = proximo_status(status)
for i in range(3):
    print(status)
    status = proximo_status(status)
