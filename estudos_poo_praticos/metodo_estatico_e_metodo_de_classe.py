class Temperatura:
    def __init__(self, celsius) -> None:
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        return cls(round((fahrenheit - 32) / 1.8, 1))

    @staticmethod
    def celsius_para_fahrenheit(celsius):
        return round(celsius * 1.8 + 32, 1)


t1 = Temperatura(25)
print(t1.celsius)  # 25

t2 = Temperatura.from_fahrenheit(98.6)
print(t2.celsius)  # 37.0 (aproximadamente)

print(Temperatura.celsius_para_fahrenheit(0))  # 32.0
