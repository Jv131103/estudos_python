def busca_simples(lista, alvo):
    cont = 0
    posicoes = []
    for idx, valor in enumerate(lista):
        if valor == alvo:
            posicoes.append(idx)
            cont += 1

    return cont, posicoes if posicoes else [None, None]


def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1

    encontrado = None

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if lista[meio] == alvo:
            encontrado = meio
            break

        elif lista[meio] < alvo:
            esquerda = meio + 1

        else:
            direita = meio - 1

    if encontrado is None:
        return 0, [None, None]

    inicio = encontrado
    fim = encontrado

    while inicio > 0 and lista[inicio - 1] == alvo:
        inicio -= 1

    while fim < len(lista) - 1 and lista[fim + 1] == alvo:
        fim += 1

    posicoes = []

    for i in range(inicio, fim + 1):
        posicoes.append(i)

    cont = len(posicoes)

    return cont, posicoes


def trata_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um valor numérico inteiro")


def trata_input_pergunta(msg):
    while True:
        dado = input(msg).strip().lower().replace("ã", "a")
        if not dado:
            print("Digite algo...")
            continue

        if dado not in ["sim", "nao"]:
            print("Digite apenas valores 'sim' ou 'nao'")
            continue

        return dado


def trata_input_busca(msg):
    while True:
        dado = input(msg).strip().lower().replace("á", "a")
        if not dado:
            print("Digite algo...")
            continue

        if dado not in ["binaria", "linear"]:
            print("Digite apenas valores 'binaria' ou 'linear'")
            continue

        return dado


def main():
    while True:

        while True:
            n = trata_int("Quantos números quer informar? ")
            if n > 0:
                break

            print("Informe pelo menos 1 número.")

        lista = []

        for v in range(n):
            lista.append(trata_int(f"Número {v + 1}: "))

        print()

        valor_a_procurar = trata_int("Número a pesquisar: ")

        tipo_de_busca = trata_input_busca("Tipo de busca [BINARIA | LINEAR]: ")
        if tipo_de_busca == "linear":
            total, posicoes = busca_simples(lista, valor_a_procurar)
        elif tipo_de_busca == "binaria":
            total, posicoes = busca_binaria(lista, valor_a_procurar)

        if total > 0:
            print(f"O número {valor_a_procurar} foi encontrado {total} vezes.")
            indice0, indice_final = posicoes[0], posicoes[len(posicoes) - 1]
            print(f"Primeira posição: {indice0}")
            print(f"Última posição:: {indice_final}")
        else:
            print(f"O número {valor_a_procurar} não foi encontrado.")
        print()

        continuar = trata_input_pergunta("QUER CONTINUAR? ")
        if continuar == "nao":
            break

        print()


main()
