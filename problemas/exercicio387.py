class ContadorLimitado:
    def __init__(self, limite) -> None:
        if limite <= 0:
            raise ValueError("Limite deve ser maior que zero!")
        self.limite = limite
        self.contador = 0

    def incrementar(self):
        if self.contador < self.limite:
            print("Adicionando + 1")
            self.contador += 1
            return True
        print("Contador atingiu o seu limite!")
        return False

    @property
    def valor(self):
        return self.contador


c = ContadorLimitado(4)
c.incrementar()
c.incrementar()
c.incrementar()
c.incrementar()
c.incrementar()
print(c.valor)
