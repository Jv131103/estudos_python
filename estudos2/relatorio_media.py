def relatorio_notas():
    n = int(input())

    notas = []
    aprovados = 0

    while len(notas) < n:
        try:
            nota = float(input())
        except ValueError:
            continue

        if not (0 <= nota <= 10):
            # regra escolhida: pedir de novo (ignora a entrada inválida)
            continue

        notas.append(nota)
        if nota >= 7:
            aprovados += 1

    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)

    print(f"Maior: {maior:.1f}")
    print(f"Menor: {menor:.1f}")
    print(f"Media: {media:.2f}")
    print(f"Aprovados: {aprovados}")


relatorio_notas()
