class Carro:
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo

    @staticmethod
    def km_para_milhas(km):
        return km * 0.62137119


c1 = Carro("Mitsubishi", "Lancer Evo")
print(c1.km_para_milhas(120))
