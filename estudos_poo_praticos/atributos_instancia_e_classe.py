class Pessoa:
    especie = "Humano"  # Atributo de classe

    def __init__(self, nome):
        self.nome = nome  # Atributo de instância


p1 = Pessoa("João")
p2 = Pessoa("Ana")

print(p1.nome)
print(p2.nome)

print(p1.especie)
print(p2.especie)
