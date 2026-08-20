class NumerosPrimos:
    def __init__(self, limite=20) -> None:
        self.limite = limite
        self.atual = 2

    def __iter__(self):
        return self

    def __next__(self):
        while self.atual <= self.limite:
            candidato = self.atual
            self.atual += 1  # Prepara o próximo para a próxima chamada

            # Testa se 'candidato' é primo
            eh_primo = True
            for i in range(2, int(candidato**0.5) + 1):
                if candidato % i == 0:
                    eh_primo = False
                    break

            if eh_primo:
                return candidato

        raise StopIteration


primos = NumerosPrimos()
it = iter(primos)
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 5
print(next(it))  # 7
print(next(it))  # 11
