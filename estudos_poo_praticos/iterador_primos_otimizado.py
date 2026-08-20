class NumerosPrimos:
    def __init__(self, limite=None) -> None:
        self.atual = 1  # começa em 1 porque o primeiro passo do __next__ já incrementa pra 2
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.atual += 1

            if self.limite is not None and self.atual > self.limite:
                raise StopIteration

            if self._eh_primo(self.atual):
                return self.atual

    def _eh_primo(self, numero):
        if numero < 2:
            return False
        if numero == 2:
            return True
        if numero % 2 == 0:
            return False  # já eliminou todos os pares de uma vez

        # só precisa testar divisores ímpares, e só até a raiz quadrada
        for divisor in range(3, int(numero ** 0.5) + 1, 2):
            if numero % divisor == 0:
                return False

        return True


primos = NumerosPrimos()
it = iter(primos)
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 5
print(next(it))  # 7
print(next(it))  # 11
