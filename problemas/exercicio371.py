class Cofre:
    def __init__(self, segredo: str) -> None:
        self.__segredo = segredo
        self.__aberto = False

    def abrir(self, senha):
        if senha == self.__segredo and not self.__aberto:
            self.__aberto = True
            return True
        return False

    def fechar(self):
        if self.__aberto:
            self.__aberto = False
            return True
        return False

    @property
    def status(self):
        return "Aberto" if self.__aberto else "Fechado"


c1 = Cofre("ABCDE123")
c1.fechar()
c1.abrir("kudfghjksl")
print(c1.status)
c1.abrir("ABCDE123")
print(c1.status)
c1.fechar()
print(c1.status)
