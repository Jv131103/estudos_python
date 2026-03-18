import timeit


def modelo1(numero):
    if not isinstance(numero, (int, float)):
        return print("Tipo inválido")

    if numero > 0:
        numero = -numero
    return numero


def modelo2(numero):
    if not isinstance(numero, (int, float)):
        return print("Tipo inválido")

    if numero > 0:
        numero = numero * (-1)
    return numero


def benchmark():
    testes = {
        "modelo1 (negacao direta)": modelo1,
        "modelo2 (multiplicacao por -1)": modelo2,
    }

    iteracoes_lista = [1_000, 10_000, 100_000, 1_000_000, 5_000_000]
    numero_teste = 42

    print("=" * 65)
    print("BENCHMARK — modelo1 vs modelo2")
    print("Big-O: O(1) para ambas as funcoes")
    print("=" * 65)

    resultados = {nome: [] for nome in testes}

    for iteracoes in iteracoes_lista:
        print(f"\nIteracoes: {iteracoes:,}")
        print("-" * 40)

        for nome, func in testes.items():
            tempo_total = timeit.timeit(
                lambda f=func: f(numero_teste),
                number=iteracoes
            )
            tempo_ns = (tempo_total / iteracoes) * 1e9
            resultados[nome].append(tempo_ns)
            print(f"  {nome:<35} {tempo_ns:7.2f} ns/chamada")

    print("\n" + "=" * 65)
    print("RESUMO — Media por funcao")
    print("=" * 65)
    for nome, tempos in resultados.items():
        media = sum(tempos) / len(tempos)
        print(f"  {nome:<35} {media:7.2f} ns (media)")

    nomes = list(resultados.keys())
    if len(nomes) == 2:
        medias = [sum(v) / len(v) for v in resultados.values()]
        delta = medias[1] - medias[0]
        mais_rapida = nomes[0] if delta >= 0 else nomes[1]
        print(f"\n  Diferenca media: {abs(delta):.2f} ns")
        print(f"  Mais rapida: {mais_rapida}")

    print("\n" + "=" * 65)
    print("ANALISE BIG-O")
    print("=" * 65)
    print("  modelo1: O(1) — usa UNARY_NEGATIVE (-n), 1 instrucao")
    print("  modelo2: O(1) — usa BINARY_MULTIPLY (n*-1), 2 operandos")
    print("  Ambas sao tempo constante. modelo1 e mais idiomatico em Python.")
    print("=" * 65)


if __name__ == "__main__":
    benchmark()
