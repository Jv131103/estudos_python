from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def calcular_autonomia(self):
        pass

    @abstractmethod
    def tipo_combustivel(self):
        pass

    def descricao(self):
        print(f"{self.marca} {self.modelo} ({self.ano})")
        print(f"Combustível: {self.tipo_combustivel()}")
        print(f"Autonomia: {self.calcular_autonomia()} KM", end=" ")


class CarroEletrico(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_bateria, consumo):
        super().__init__(marca, modelo, ano)
        self.capacidade_bateria = capacidade_bateria
        self.consumo = consumo

    def calcular_autonomia(self):
        auto = int(round(self.capacidade_bateria * self.consumo, 0))
        return auto

    def tipo_combustivel(self):
        return "Elétrico"


class CarroFlex(Veiculo):
    def __init__(self, marca, modelo, ano, tanque, consumo_gasolina, consumo_etanol):
        super().__init__(marca, modelo, ano)
        self.tanque = tanque
        self.consumo_gasolina = consumo_gasolina
        self.consumo_etanol = consumo_etanol

    def calcular_autonomia(self):
        auto = int(round(max(self.tanque * self.consumo_gasolina, self.tanque * self.consumo_etanol), -1))
        return auto

    def tipo_combustivel(self):
        return "Flex (Gasolina/Etanol)"


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tanque, consumo):
        super().__init__(marca, modelo, ano)
        self.tanque = tanque
        self.consumo = consumo

    def calcular_autonomia(self):
        auto = int(round(self.tanque * self.consumo, 0))
        return auto

    def tipo_combustivel(self):
        return "Gasolina"


def interface():
    # Cria os objetos uma vez
    veiculos = [
        ("🚗", CarroEletrico("Tesla", "Model 3", "2023", 57.5, 8.35)),
        ("🚗", CarroFlex("Fiat", "Pulse", "2022", 47, 12.8, 9.0)),
        ("🏍️", Moto("Honda", "CB500", "2021", 17.1, 20.46)),
    ]

    # Acha o maior sem loop explícito
    mais_autonomo = max(v.calcular_autonomia() for _, v in veiculos)

    # Exibe — um loop só
    for emoji, veiculo in veiculos:
        print(f"\n{emoji}  ", end="")
        veiculo.descricao()
        if veiculo.calcular_autonomia() == mais_autonomo:
            print(" (melhor opção)")
        else:
            print()


interface()
