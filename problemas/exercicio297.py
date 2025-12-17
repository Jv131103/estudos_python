class Relogio:
    def __init__(self, horas, minutos) -> None:
        self.horas = horas
        self.minutos = minutos

    def avancar_minutos(self):
        if self.horas == 24:
            self.horas -= 23

        if self.minutos == 59:
            self.minutos = 0
            self.horas += 1
        else:
            self.minutos += 1

    def ver(self):
        print(f"Agora são: {self.horas}:{self.minutos:02}")


relogio = Relogio(15, 44)

for i in range(360):
    relogio.ver()
    relogio.avancar_minutos()
