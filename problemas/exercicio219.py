def contar_linhas_validas(caminho):
    cont = 0
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if not linha:
                continue

            if linha.startswith("#"):
                continue

            cont += 1

    return cont


print(contar_linhas_validas("./arquivos/dados.txt"))
