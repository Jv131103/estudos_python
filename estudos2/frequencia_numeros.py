def frequencia_numeros(numeros, tipo="get"):
    dicionario = {}

    if tipo == "get":
        for numero in numeros:
            dicionario[numero] = dicionario.get(numero, 0) + 1
    else:
        for numero in numeros:
            if numero in dicionario:
                dicionario[numero] += 1
            else:
                dicionario[numero] = 1

    return dicionario


def frequencia_numeros_lista(numeros):
    lista_maior = []

    i = 0

    ja_foi = []
    while i < len(numeros):
        valor = numeros[i]
        if valor in ja_foi:
            i += 1
            continue
        else:
            ja_foi.append(valor)

        lista = [valor, 1]

        for j in range(i + 1, len(numeros)):
            if valor == numeros[j]:
                lista[-1] += 1
            else:
                continue

        lista_maior.append(lista)
        i += 1

    return lista_maior


def mais_frequentes(frequencias):
    if isinstance(frequencias, dict):
        dados = frequencias.items()
    else:
        dados = frequencias

    maior_frequencia = 0
    numeros_mais_frequentes = []

    for numero, frequencia in dados:
        if frequencia > maior_frequencia:
            maior_frequencia = frequencia
            numeros_mais_frequentes = [numero]

        elif frequencia == maior_frequencia:
            numeros_mais_frequentes.append(numero)

    return numeros_mais_frequentes, maior_frequencia


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

        if dado not in ["dict", "list"]:
            print("Digite apenas valores 'dict' ou 'list'")
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

        tipo_de_busca = trata_input_busca("Tipo de busca [DICT | LIST]: ")
        if tipo_de_busca == "dict":
            frequencias = frequencia_numeros(lista)
        elif tipo_de_busca == "list":
            frequencias = frequencia_numeros_lista(lista)

        loop = frequencias.items() if isinstance(frequencias, dict) else frequencias

        for chave, valor in loop:
            print(f"{chave} apareceu {valor} vez(es)")

        print()
        numeros, quantidade = mais_frequentes(frequencias)
        print(f"Números mais frequentes: {numeros}")
        print(f"Quantidade: {quantidade}")

        print()

        continuar = trata_input_pergunta("QUER CONTINUAR? ")
        if continuar == "nao":
            break

        print()


main()
