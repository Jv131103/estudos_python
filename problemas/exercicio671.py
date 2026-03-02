"""
Você deve elaborar um algoritmo implementado em Python em que o usuário
precisa informar quantos alimentos ele consumiu naquele dia e em seguida
possa informar o número de calorias de cada um dos alimentos. Como não
estudamos listas neste capítulo, você não precisa se preocupar em armazenar
todas as calorias digitadas, mas no final é necessário exibir o total de
calorias consumidas.
"""


def main():
    try:
        qtd_consumidos = int(input("Quantos alimentos consumiu? "))
        if qtd_consumidos <= 0:
            print("A quantidade deve ser positiva e maior que 0.")
            return

        total_calorias = 0

        for qtd in range(1, qtd_consumidos + 1):
            while True:
                try:
                    calorias = int(input(f"Quantidade de calorias no alimento {qtd}: "))
                    if calorias < 0:
                        print("Não existe alimento não calórico, digite calorias positivas")
                        continue
                    break
                except ValueError:
                    print("Calorias precisa ser número")
            total_calorias += calorias

        print(f"Você consumiu {total_calorias} calorias hoje")

    except ValueError:
        print("Digite apenas números")


main()
