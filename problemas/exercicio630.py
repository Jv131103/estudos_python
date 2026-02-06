"""
Termostato com validação via property

Crie uma classe termostato que vai envolver:

    Atributo “privado”: __temperatura (começa em 20)

    precisa obter getters e setters

        Setter deve aceitar apenas int/float

    Impedir temperatura fora do intervalo [10, 30] (raise ValueError)

    Método aumentar(delta) e diminuir(delta) usando a property (não acessar _temperatura direto)

Teste rápido

    tentar setar -5 → erro

    aumentar(3) → 23
"""


class Termostato:
    """
    SIMULA UM TERMOSTATO REAL

        Não possui parâmetros de acesso

        - padrão temperatura: 20

    retorna o status atual dele

    Limitações:

        - Não pode acessar temperatura em seu modo privado

        - inserção de temperatura, aumento e diminuição precisam ser objetos numéricos

        - temperatura é limitante no intervalo de [10, 30]

        - Erros externos de aumentar e diminuir, retornam em formato log(estético apenas)

    """
    def __init__(self) -> None:
        self.__temperatura: int | float = 20

    @property
    def temperatura(self) -> int | float:
        """Interface que retorna a temperatura atual"""
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor: int | float) -> None:
        """
        Regra do projeto. Aqui onde o tratatamento do termostato é executado

        PS: Não altere valores de tratamento de erros.
        """
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser do tipo numérico")

        if valor < 10 or valor > 30:
            raise ValueError("Valor precisa estar entre [10, 30]")

        self.__temperatura = valor

    def aumentar(self, delta: int | float) -> bool:
        """
        Aumenta a temperatura em delta mais a temperatura atual
        """
        try:
            self.temperatura += delta
            return True
        except ValueError as ve:
            print(ve)
            return False

    def diminuir(self, delta: int | float) -> bool:
        """
        Diminui a temperatura em delta menos a temperatura atual
        """
        try:
            self.temperatura -= delta
            return True
        except ValueError as ve:
            print(ve)
            return False

    def __str__(self) -> str:
        return f"Temperarura atual: {self.temperatura:.2f} °C"


if __name__ == "__main__":
    termostato = Termostato()
    # termostato.temperatura = -5
    termostato.aumentar(3)
    print(termostato)
    termostato.aumentar(300)
