class Impressora:
    def executar(self):
        print("Imprimindo documento")


class Scanner:
    def executar(self):
        print("Escaneando documento")


def sistema(objeto):
    objeto.executar()


sistema(Impressora())
sistema(Scanner())
