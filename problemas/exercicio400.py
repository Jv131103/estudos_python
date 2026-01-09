def modelo_manual():

    soma = 0
    maior = 0
    menor = 10
    qtd_notas = 0
    aprovados = 0

    while True:
        try:
            n = float(input())
            if n < 0:
                break
        except ValueError:
            print("Tipo Inválido")
            continue

        if n > maior:
            maior = n

        if n < menor:
            menor = n

        if n >= 7:
            aprovados += 1

        soma += n
        qtd_notas += 1

    media = soma / qtd_notas
    print(f"MAIOR: {maior}")
    print(f"MENOR: {menor}")
    print(f"MÉDIA: {media:.2f}")
    print(f"Aprovados: {aprovados}")


def modelo_lista():
    lista = []

    aprovados = 0
    while True:
        try:
            n = float(input())
            if n < 0:
                break

            if n >= 7:
                aprovados += 1

            lista.append(n)
        except ValueError:
            print("Tipo Inválido")
            continue

    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)

    print(f"MAIOR: {maior}")
    print(f"MENOR: {menor}")
    print(f"MÉDIA: {media:.2f}")
    print(f"Aprovados: {aprovados}")


modelo_lista()
