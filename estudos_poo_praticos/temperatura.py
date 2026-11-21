
class Termostato:
    def __init__(self, temperatura: int | float) -> None:
        # Passa pelo setter para validar a temperatura inicial
        self.temperatura = temperatura

    @property
    def temperatura(self) -> int | float:
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nova_temperatura: int | float) -> None:
        if isinstance(nova_temperatura, bool) or not isinstance(
            nova_temperatura, (int, float)
        ):
            raise TypeError("Temperatura precisa ser numérica")

        if not (16 <= nova_temperatura <= 30):
            raise ValueError("Temperatura precisa estar entre 16 e 30 graus")

        self.__temperatura = nova_temperatura

    def aumentar_temperatura(self, graus: int | float) -> int | float:
        if isinstance(graus, bool) or not isinstance(graus, (int, float)):
            raise TypeError("Graus precisa ser numérico")

        if graus <= 0:
            raise ValueError("O aumento precisa ser maior que zero")

        # A alteração passa pelo setter automaticamente
        self.temperatura += graus

        return self.temperatura


if __name__ == "__main__":
    termostato = Termostato(22)

    print("Temperatura inicial:", termostato.temperatura)

    termostato.temperatura = 25
    print("Temperatura alterada:", termostato.temperatura)

    print("Temperatura após aumento:", termostato.aumentar_temperatura(3))
