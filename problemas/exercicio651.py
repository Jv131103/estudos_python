"""
Crie um Enum Semaforo com:

    VERDE

    AMARELO

    VERMELHO

E use match para definir próxima cor.
"""

from enum import Enum


class Semaforo(Enum):
    VERDE = 1
    AMARELO = 2
    VERMELHO = 3

    def mudar_sinal(self):
        match self:
            case Semaforo.VERDE:
                return Semaforo.AMARELO
            case Semaforo.AMARELO:
                return Semaforo.VERMELHO
            case Semaforo.VERMELHO:
                return Semaforo.VERDE


sinal = Semaforo.VERDE
for i in range(3):
    print(sinal)
    sinal = sinal.mudar_sinal()
