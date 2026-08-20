class Veiculo:
    def __init__(self, modelo, placa, valor_diaria=0.0) -> None:
        self.modelo = modelo
        self.placa = placa
        self.valor_diaria = valor_diaria
        self.disponivel = True

    def alugar(self):
        if not self.disponivel:
            raise ValueError("Veículo já alugado!")

        self.disponivel = False

    def devolver(self):
        if self.disponivel:
            raise ValueError("Veículo já encontra-se devolvido!")

        self.disponivel = True

    def calcular_valor_aluguel(self):
        raise ValueError("Não se pode chamar direto da classe Veículo!")


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria=0.0, numero_portas=4) -> None:
        super().__init__(modelo, placa, valor_diaria)
        self.numero_portas = numero_portas

    def calcular_valor_aluguel(self, dias):
        valor = self.valor_diaria
        if dias >= 7:
            valor = valor - (valor * 0.1)
        return valor * dias


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria=0.0, cilindradas=90) -> None:
        super().__init__(modelo, placa, valor_diaria)
        self.cilindradas = cilindradas

    def calcular_valor_aluguel(self, dias):
        return self.valor_diaria * dias + 20


class Locadora:
    def __init__(self) -> None:
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def veiculos_disponiveis(self):
        print("==" * 30)
        for veiculo in self.veiculos:
            if veiculo.disponivel:
                print(veiculo.modelo)
                print(veiculo.placa)
                print("++" * 30)

    def alugar_veiculo(self, placa, dias):
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                veiculo.alugar()
                return veiculo.calcular_valor_aluguel(dias)

        raise ValueError("Placa não encontrada!")


locadora = Locadora()
locadora.adicionar_veiculo(Carro("Onix", "ABC-1234", 150.00, numero_portas=4))
locadora.adicionar_veiculo(Moto("CB500", "XYZ-9876", 80.00, cilindradas=500))

print(locadora.alugar_veiculo("ABC-1234", 10))  # com desconto de 10%
print(locadora.alugar_veiculo("XYZ-9876", 3))   # com taxa fixa de seguro
