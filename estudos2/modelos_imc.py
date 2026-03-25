def modelo1():
    # 1
    nome = input("Nome: ")
    peso = float(input("Peso [Kg]: "))
    altura = float(input("Altura [M]: "))

    # 2
    imc = peso / altura**2

    # 3
    print(f"Seu nome é: {nome}")
    print(f"Seu IMC é de {imc:.2f}")

    # 4
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Peso normal")
    elif 25 <= imc <= 30:
        print("Sobrepeso")
    else:
        print("Obesidade")


def modelo2():
    # 1
    nome = input("Nome: ")
    peso = float(input("Peso [Kg]: "))
    altura = float(input("Altura [M]: "))

    # 2
    imc = peso / altura**2

    # 3
    print(f"Seu nome é: {nome}")
    print(f"Seu IMC é de {imc:.2f}")

    # 4
    tabela = [
        (0, 18.5, "Abaixo do peso"),
        (18.5, 25, "Peso normal"),
        (25, 30, "Sobrepeso"),
        (30, float("inf"), "Obesidade")
    ]

    for minimo, maximo, resultado in tabela:
        if minimo <= imc < maximo:
            print(resultado)
            break


modelo1()
# modelo2()
