class Temporizador:
    def __init__(self, minutos):
        if minutos < 0:
            raise ValueError("Minutos não podem ser negativos")
        self.minutos = minutos

    def zerado(self):
        return self.minutos == 0

    def tic(self):
        if self.minutos > 0:
            self.minutos -= 1

    def formatado(self):
        horas = self.minutos // 60
        minutos = self.minutos % 60
        return f"{horas:02d}:{minutos:02d}"


tempo = 125
temp = Temporizador(tempo)

for _ in range(tempo + 1):
    print(temp.formatado())
    temp.tic()
