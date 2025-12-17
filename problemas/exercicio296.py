class Cor:
    def vermelho(self):
        return "vermelho"

    def amarelo(self):
        return "amarelo"

    def verde(self):
        return "verde"


class Semaforo:
    def __init__(self) -> None:
        self.cor = Cor().vermelho()

    def status(self):
        return self.cor

    def mudar(self):
        match self.status():
            case "vermelho":
                self.cor = Cor().verde()
            case "verde":
                self.cor = Cor().amarelo()
            case "amarelo":
                self.cor = Cor().vermelho()
            case _:
                print("Semáforo desligado")

        return self.status()


semaforo_av_x = Semaforo()
print(semaforo_av_x.mudar())
print(semaforo_av_x.mudar())
print(semaforo_av_x.mudar())
print(semaforo_av_x.mudar())
print(semaforo_av_x.mudar())
print(semaforo_av_x.mudar())
