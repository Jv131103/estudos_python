def parse_pessoa(linha):
    # decide separador
    if "," in linha:
        partes = linha.split(",")
    elif ";" in linha:
        partes = linha.split(";")
    else:
        return None

    # valida quantidade de campos
    if len(partes) != 3:
        return None

    nome = partes[0].strip()
    idade_str = partes[1].strip()
    cidade = partes[2].strip()

    # valida idade
    try:
        idade = int(idade_str)
    except ValueError:
        return None

    return (nome, idade, cidade)


linha = input()
resultado = parse_pessoa(linha)

if resultado is None:
    print("FORMATO INVALIDO")
else:
    nome, idade, cidade = resultado
    print(nome, idade, cidade)
