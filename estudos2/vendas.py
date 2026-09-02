import csv
from pathlib import Path

pasta = Path("./csvs")
pasta.mkdir(exist_ok=True)

ARQUIVO = pasta / "vendas2.csv"


def criar_csv_exemplo():
    if not ARQUIVO.exists():
        dados = [
            ["produto", "quantidade", "preco_unitario"],
            ["Teclado", "2", "150.00"],
            ["Mouse", "5", "80.50"],
            ["Monitor", "1", "1200.00"],
        ]
        with open(ARQUIVO, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(dados)


def vendas_processadas():
    criar_csv_exemplo()

    total_geral = 0.0
    linhas_processadas = []

    with open(ARQUIVO, mode="r", newline="", encoding="utf-8") as f:
        leitor = csv.DictReader(f)

        for linha in leitor:
            produto = linha["produto"]
            quantidade = int(linha["quantidade"])
            preco_unitario = float(linha["preco_unitario"])

            subtotal = quantidade * preco_unitario
            total_geral += subtotal

            linha["valor_total"] = f"{subtotal:.2f}"
            linhas_processadas.append(linha)

    # Escreve o novo arquivo com a coluna extra
    arquivo_saida = pasta / "vendas_processadas.csv"
    with open(arquivo_saida, mode="w", newline="", encoding="utf-8") as f:
        campos = ["produto", "quantidade", "preco_unitario", "valor_total"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(linhas_processadas)

    print(f"FATURAMENTO TOTAL: R$ {total_geral:.2f}")
    return arquivo_saida


vendas_processadas()
