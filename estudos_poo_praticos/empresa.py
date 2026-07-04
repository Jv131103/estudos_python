class Endereco:
    def __init__(self, rua, cidade, cep) -> None:
        self.rua = rua
        self.cidade = cidade
        self.cep = cep


class Empresa:
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco

    @classmethod
    def from_dict(cls, dados):
        endereco = Endereco(**dados["endereco"])

        return cls(
            dados.get("nome", "SEM NOME"),
            dados.get("cnpj", "SEM CNPJ"),
            endereco
        )

    def __str__(self):
        return (
            f"{self.nome} ({self.cnpj})\n"
            f"{self.endereco.rua}, "
            f"{self.endereco.cidade} - "
            f"{self.endereco.cep}"
        )


dados = {
    "nome": "TechCorp",
    "cnpj": "12.345.678/0001-99",
    "endereco": {"rua": "Av. Paulista", "cidade": "São Paulo", "cep": "01310-100"}
}

empresa = Empresa.from_dict(dados)
print(empresa)
# TechCorp (12.345.678/0001-99)
# Av. Paulista, São Paulo — CEP: 01310-100
