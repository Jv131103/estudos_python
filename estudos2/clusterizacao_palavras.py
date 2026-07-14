palavras = [
    "casa",
    "python",
    "sol",
    "computador",
    "lua",
    "janela",
    "uva"
]

clusters = {}

for palavra in palavras:
    tamanho = len(palavra)

    clusters.setdefault(tamanho, []).append(palavra)

print(clusters)
