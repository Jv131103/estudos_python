# Abre o arquivo em modo Escrita
arq = open("./arquivos/arquivo.txt", "w")
# Grava a primeira linha
arq.write("A")
# Grava segunda linha
arq.write("B")  # No caso tudo na mesma linha
# Fecha o arquivo
arq.close()
