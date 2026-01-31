"""
Faça um programa que:

    Tente ler um arquivo chamado config.txt

    Se o arquivo existir:

        use o conteúdo dele como configuração

    Se o arquivo não existir:

        use uma configuração padrão definida no código

Mostre qual configuração foi usada
"""


CONFIG_PADRAO = {
    "modo": "desenvolvimento",
    "debug": True,
    "porta": 8080
}


def carregar_config(nome_arquivo="config.txt"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as file:
            print("Configuração carregada do arquivo:")
            config = file.read().strip()
            print(config)
            return config
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        print("Usando configuração padrão:")
        print(CONFIG_PADRAO)
        return CONFIG_PADRAO


carregar_config("config.txt")
