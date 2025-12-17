class Relogio:
    def __init__(self, hora, minuto) -> None:
        self.hora = hora
        self.minuto = minuto

    def avancar_minuto(self):
        self.minuto += 1
        if self.minuto == 60:
            self.minuto = 0
            self.hora = (self.hora + 1) % 24

    def ver(self):
        return f"{self.hora:02}:{self.minuto:02}"


relogio = Relogio(00, 00)

for i in range(360):
    print(relogio.ver())
    relogio.avancar_minuto()
