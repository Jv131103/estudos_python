def parse_pessoa(linha):
    if "," in linha:
        return linha.split(",")
    elif ";" in linha:
        return linha.split(";")
    else:
        return "FORMATO INVÁLIDO!"


def saida(informacao):
    if informacao == "FORMATO INVÁLIDO!":
        print("FORMATO INVÁLIDO!")

    if len(informacao) == 3:
        nome, idade, cidade = informacao

        nome = nome.strip()
        cidade = cidade.strip()
        try:
            idade = int(idade.strip())
            print(nome, idade, cidade)
        except ValueError:
            print("Tipo inválido para idade")
    else:
        print("INFORMAÇÃO POSSUI MUITAS INFORMAÇÕES, O VPÁLIDO É [NOME],[IDADE],[ESTADO]")


linha = input()
informacao = parse_pessoa(linha)
saida(informacao)
