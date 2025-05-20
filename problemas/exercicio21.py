"""
Dada uma lista de entradas de usuário de números inteiros, construa um
dicionário com:
    - A lista padrão
    - A lista dos valores elevados ao quadrado
    - A lista dos valores elevados ao cubo
"""

iniciar = "s"

while iniciar.lower() in ["s", "sim"]:
    lista = []
    d = {}

    while True:
        numero = input("Digite um número: [! - sair] ")

        if numero == "!":
            break

        try:
            numero = int(numero)
        except ValueError:
            print("Erro!\nDigite apenas NÚMEROS\nou ! para sair.")
            continue  # ❗ Importante: pula para a próxima iteração

        lista.append(numero)

    # Criando o dicionário com as três versões da lista
    d["padrao"] = lista
    d["quadrado"] = [n**2 for n in lista]
    d["cubo"] = [n**3 for n in lista]

    print("\nResultado:")
    for chave, valores in d.items():
        print(f"{chave.capitalize()}: {valores}")
    print()

    iniciar = input("\nDeseja continuar? [s/n] ")
