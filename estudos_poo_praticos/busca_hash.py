class BuscaHash:
    def __init__(self, dicionario) -> None:
        self.normal = dicionario
        self.reverso = {v: k for k, v in dicionario.items()}

    def buscar(self, alvo):
        if alvo in self.normal:
            return self.normal[alvo]

        if alvo in self.reverso:
            chave = self.reverso[alvo]
            return self.normal[chave]

        return None


usuarios = BuscaHash(
    {
        "joao": 123,
        "maria": 456,
        "ana": 789
    }
)

print(usuarios.buscar("joao"))
print(usuarios.buscar(123))
