def mode1(idade):
    if 18 <= idade <= 115:
        print("Maior de idade")
    elif 0 <= idade <= 17:
        print("Menor de idade")
    else:
        print("Idade inválida!")


def mode2(idade):
    table = [
        (18, 115, "Maior de idade"),
        (0, 17, "Menor de idade"),
    ]

    for inicio, fim, saida in table:
        if inicio <= idade <= fim:
            print(saida)
            break
    else:
        print("Idade inválida!")


testes = list(range(-8, 120, 2))

for teste in testes:
    print("idade:", teste)
    mode2(teste)
    print()
