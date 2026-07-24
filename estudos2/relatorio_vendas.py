import csv


def carregar_vendas(caminho_arquivo="vendas.csv"):
    """Lê o arquivo CSV e retorna uma lista de dicionários."""
    vendas = []
    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            vendas.append(linha)
    return vendas


def total_por_categoria(vendas):
    """Soma o valor total vendido por cada categoria."""
    totais = {}
    for venda in vendas:
        categoria = venda["categoria"]
        # Convertemos o valor para float (número decimal) para poder somar
        valor = float(venda["valor"])

        # Se a categoria já existe no dicionário, soma. Se não, cria.
        if categoria in totais:
            totais[categoria] += valor
        else:
            totais[categoria] = valor

    return totais


def exportar_relatorio(totais, caminho_saida="./csvs/relatorio_categorias.csv"):
    """Salva um novo CSV contendo apenas as categorias e os totais."""
    with open(caminho_saida, mode="w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)

        # Escreve o cabeçalho (nome das colunas)
        escritor.writerow(["categoria", "total_vendido"])

        # Escreve cada linha com o nome da categoria e o valor formatado
        for categoria, total in totais.items():
            escritor.writerow([categoria, round(total, 2)])

    print(f"Relatório exportado com sucesso para '{caminho_saida}'!")


# 1. Carrega os dados
dados_vendas = carregar_vendas("./csvs/vendas.csv")

# 2. Processa os totais
totais_categoria = total_por_categoria(dados_vendas)

# 3. Exporta o resultado
exportar_relatorio(totais_categoria)
