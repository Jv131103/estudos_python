"""
Crie um LogMixin e use em duas classes diferentes.
"""


class LogMixin:
    def log(self, msg):
        return f"[LOG] {msg}"


class Imprimir(LogMixin):
    def imprimir(self, documento):
        print(self.log(f"Imprimindo {documento}..."))


class Veiculo(LogMixin):
    def __init__(self, nome) -> None:
        self.nome = nome

    def registrar(self):
        print(self.log(f"Registrando o veículo {self.nome}..."))


impressora = Imprimir()
impressora.imprimir("./estudos_python/requiriments.txt")

carro = Veiculo("Civic")
carro.registrar()
