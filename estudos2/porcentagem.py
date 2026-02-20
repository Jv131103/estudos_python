def ler_numero(text):
    return float(input(text).replace(",", "."))


while True:
    try:
        valor = ler_numero("Valor: [0 - sai do programa] ")
        if valor == 0:
            break
        porcentagem = ler_numero("Porcentagem: ")

        percentual = valor * porcentagem / 100
        acrescimo = percentual + valor
        desconto = valor - percentual
    except ValueError:
        print("Digite apenas números")
        continue

    print()
    print(f"Percentual: {percentual}")
    print(f"Acréscimo: {acrescimo}")
    print(f"Desconto: {desconto}")
    print()
