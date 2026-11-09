def maior_aumento(precos):
    result = {
        "aumento": 0,
        "dia_inicial": None,
        "dia_final": None
    }

    i = 1

    while i < len(precos):
        valor = precos[i] - precos[i - 1]
        if valor > result["aumento"]:
            result["aumento"] = valor
            result["dia_inicial"] = i - 1
            result["dia_final"] = i

        i += 1

    return result


testes = [
    ([], 0, None, None),
    ([100], 0, None, None),
    ([10, 25], 15, 0, 1),
    ([50, 50, 50, 50], 0, None, None),
    ([100, 80, 60, 40, 20], 0, None, None),
    ([100, 105, 103, 112, 110], 9, 2, 3),
    ([10, 12, 14, 100], 86, 2, 3),
    ([4, 7, 10], 3, 0, 1),
    ([0, 100, 0, 200], 200, 2, 3),
    ([1000, 1, 1002], 1001, 1, 2),
    ([7, 7, 7, 8], 1, 2, 3),
    ([999999999, 1000000000, 999999998], 1, 0, 1),
    ([100, 20, 90, 10, 80], 70, 1, 2),
    ([3, 1, 2, 100], 98, 2, 3),
    ([50, 100, 20, 80, 30, 90], 60, 2, 3)
]

aprovados = 0

for numero, (precos, aumento, inicio, fim) in enumerate(testes, 1):
    esperado = {
        "aumento": aumento,
        "dia_inicial": inicio,
        "dia_final": fim
    }

    obtido = maior_aumento(precos)

    if obtido == esperado:
        print(f"Teste {numero:02d}: PASSOU")
        aprovados += 1
    else:
        print(f"Teste {numero:02d}: FALHOU")
        print(f"  Esperado: {esperado}")
        print(f"  Obtido:   {obtido}")

print(f"\nResultado: {aprovados}/{len(testes)} testes aprovados")
