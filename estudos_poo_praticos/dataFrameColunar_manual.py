class DataFrameColunar:
    def __init__(self, dados):
        self.dados = dados

        tamanhos = {len(valores) for valores in dados.values()}
        if len(tamanhos) > 1:
            raise ValueError("todas as colunas devem ter o mesmo tamanho")

    def colunas(self):
        return list(self.dados.keys())

    def selecionar_coluna(self, nome):
        return self.dados[nome]

    def selecionar_linha(self, indice):
        return {coluna: valores[indice] for coluna, valores in self.dados.items()}

    def __str__(self):
        colunas = self.colunas()
        n_linhas = len(next(iter(self.dados.values()), []))

        larguras = {}
        for coluna in colunas:
            maior = len(coluna)
            for valor in self.dados[coluna]:
                maior = max(maior, len(str(valor)))
            larguras[coluna] = maior

        cabecalho = " | ".join(f"{coluna:<{larguras[coluna]}}" for coluna in colunas)
        separador = "-+-".join("-" * larguras[coluna] for coluna in colunas)

        linhas_texto = []
        for i in range(n_linhas):
            linha = " | ".join(
                f"{str(self.dados[coluna][i]):<{larguras[coluna]}}" for coluna in colunas
            )
            linhas_texto.append(linha)

        return "\n".join([cabecalho, separador] + linhas_texto)


df = DataFrameColunar({
    "nome": ["Ana", "Bruno", "Carla"],
    "idade": [20, 25, 22],
    "cidade": ["SP", "RJ", "BH"]
})

print(df)
print(df.selecionar_coluna("nome"))
print(df.selecionar_linha(2))
