def categoria_e_valida(numero_categoria):
    if 1 <= numero_categoria <= 10:
        return True
    else:
        return False


def exib_dados_categoria(key, preco):
    return f"* Categoria {key} - $ {preco.replace(".", ",")}"


def precos(numero_categoria):
    if not categoria_e_valida(numero_categoria):
        return "Categória inválida... digite a opcao de 0 a 10"

    valores = [
        '0,5',
        '11,3',
        '17,5',
        '33,97',
        '103,47',
        '44,67',
        '12,55',
        '14,87',
        '98,12',
        '131,4'
    ]

    return exib_dados_categoria(numero_categoria, valores[numero_categoria - 1])


while True:
    n = int(input("digite a categoria de 1, 10 [0 para sair] "))
    if not n:
        break
    print(precos(n))
