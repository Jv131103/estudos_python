from enum import Enum


class Status(Enum):
    PENDENTE = 1
    PAGO = 2
    ENVIADO = 3

    def proximo(self):
        match self:
            case Status.PENDENTE:
                return Status.PAGO
            case Status.PAGO:
                return Status.ENVIADO
            case Status.ENVIADO:
                return Status.ENVIADO


status = Status.PENDENTE
print(status)
status = status.proximo()
print(status)
