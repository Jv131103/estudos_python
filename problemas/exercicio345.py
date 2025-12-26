class Temperatura:
    def __init__(self, celcius) -> None:
        self.celcius = celcius

    def temperatura_valida(self):
        return self.celcius >= -273.15

    def para_fahrenheit(self):
        if not self.temperatura_valida():
            return None
        return (self.celcius * 1.8) + 32

    def para_kelvin(self):
        if not self.temperatura_valida():
            return None
        return self.celcius + 273.15


temp = Temperatura(32)
print(temp.para_fahrenheit())
print(temp.para_kelvin())
