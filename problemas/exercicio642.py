"""
Crie duas classes sem herança
mas com o mesmo método
e use sub-tipagem estrutural.
"""


class SliferODragaoDosCeus:
    def __init__(self) -> None:
        self._atk = "XOOO"
        self._def = "XOOO"

    def atacar(self):
        print("Ataque de SLIFER")


class ObeliscoOAtormentador:
    def __init__(self) -> None:
        self._atk = 4000
        self._def = 4000

    def atacar(self):
        print("Ataque de OBELISCO")


class ODragaoAladoDeRa:
    def __init__(self) -> None:
        self._atk = '?'
        self._def = '?'

    def atacar(self):
        print("Ataque do DRAGÃO ALADO DE RÁ")


def atacar(card):
    card.atacar()


for cards in [SliferODragaoDosCeus(), ObeliscoOAtormentador(), ODragaoAladoDeRa()]:
    atacar(cards)
