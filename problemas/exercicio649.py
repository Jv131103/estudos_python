"""
Crie uma classe Carro com classe aninhada Motor.
"""


class Carro:
    def __init__(self, marca, modelo, ano, motor) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor

    class Motor:
        def __init__(self, modelo_motor, potencia, cilindradas, combustivel, alimentacao) -> None:
            self.modelo_motor = modelo_motor
            self.potencia = potencia
            self.cilindradas = cilindradas
            self.combustivel = combustivel
            self.alimentacao = alimentacao

        def informacoes_motor(self):
            print(f"Modelo Motor: {self.modelo_motor}")
            print(f"Potência: {self.potencia}")
            print(f"Cilindradas: {self.cilindradas}")
            print(f"Combustível: {self.combustivel}")
            print(f"Alimentação: {self.alimentacao}")

    def informacoes_veiculo(self):
        print(f"Marca: {self.marca}")
        print(f"Ano: {self.ano}")
        print(f"Modelo: {self.modelo}")
        self.motor.informacoes_motor()


motor = Carro.Motor("D16Y7", "106 cv", "1.590 cc", "Gasolina", "Injeção multiponto")
car = Carro("Honda", "Civic LX", 2000, motor)

car.informacoes_veiculo()
