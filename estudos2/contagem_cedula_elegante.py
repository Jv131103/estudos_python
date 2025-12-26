def caixa_eletronico(valor):
    valor = int(round(valor * 100))  # centavos

    notas = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5]
    resultado = {}

    for nota in notas:
        qtd = valor // nota
        if qtd > 0:
            resultado[nota] = qtd
            valor %= nota

    return resultado


def exibir(resultado):
    for nota, qtd in resultado.items():
        print(f"{qtd} nota(s) de R$ {nota / 100:.2f}")


exibir(caixa_eletronico(395.55))
