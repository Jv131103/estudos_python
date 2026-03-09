class DataFrameManual:
    def __init__(self, colunas, dados=None):
        self.colunas = colunas[:]
        self.dados = dados[:] if dados else []

    def adicionar_linha(self, linha):
        if set(linha.keys()) != set(self.colunas):
            raise ValueError("linha precisa ter exatamente as mesmas colunas")
        self.dados.append(linha)

    def selecionar_coluna(self, nome_coluna):
        if nome_coluna not in self.colunas:
            raise KeyError(f"coluna '{nome_coluna}' não existe")
        return [linha[nome_coluna] for linha in self.dados]

    def selecionar_linha(self, indice):
        return self.dados[indice]

    def filtrar(self, funcao):
        filtrados = [linha for linha in self.dados if funcao(linha)]
        return DataFrameManual(self.colunas, filtrados)

    def __str__(self):
        if not self.dados:
            return "DataFrame vazio"

        larguras = {}
        for coluna in self.colunas:
            maior = len(str(coluna))
            for linha in self.dados:
                maior = max(maior, len(str(linha[coluna])))
            larguras[coluna] = maior

        cabecalho = " | ".join(f"{coluna:<{larguras[coluna]}}" for coluna in self.colunas)
        separador = "-+-".join("-" * larguras[coluna] for coluna in self.colunas)

        linhas_texto = []
        for linha in self.dados:
            linha_formatada = " | ".join(
                f"{str(linha[coluna]):<{larguras[coluna]}}" for coluna in self.colunas
            )
            linhas_texto.append(linha_formatada)

        return "\n".join([cabecalho, separador] + linhas_texto)


df = DataFrameManual(["nome", "idade", "cidade"])

df.adicionar_linha({"nome": "Ana", "idade": 20, "cidade": "SP"})
df.adicionar_linha({"nome": "Bruno", "idade": 25, "cidade": "RJ"})
df.adicionar_linha({"nome": "Carla", "idade": 22, "cidade": "BH"})

print(df)
print(df.selecionar_coluna("idade"))
print(df.selecionar_coluna("idade")[0])


df_filtrado = df.filtrar(lambda linha: linha["idade"] >= 22)
print(df_filtrado)
