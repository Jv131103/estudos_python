"""
Implementação didática (simplificada) do algoritmo por trás do
difflib.SequenceMatcher: hash + busca do maior match + recursão.

Isso NÃO é o código real do CPython (que tem otimizações extras),
mas segue exatamente a mesma lógica e ordem de operações.
"""


def construir_hash(b):
    """Passo 1: cria um hash SÓ da sequência b -> {elemento: [posições]}"""
    b2j = {}
    for i, elemento in enumerate(b):
        b2j.setdefault(elemento, []).append(i)
    return b2j


def encontrar_maior_match(a, b, b2j):
    """Passo 2: percorre a, consulta o hash de b, acha o maior trecho contíguo igual."""
    melhor_tamanho = 0
    melhor_i = melhor_j = 0

    for i, elemento in enumerate(a):
        if elemento not in b2j:
            continue
        for j in b2j[elemento]:
            tamanho = 0
            # estende o match enquanto os elementos seguintes forem iguais
            while (i + tamanho < len(a)
                   and j + tamanho < len(b)
                   and a[i + tamanho] == b[j + tamanho]):
                tamanho += 1
            if tamanho > melhor_tamanho:
                melhor_tamanho = tamanho
                melhor_i, melhor_j = i, j

    return melhor_i, melhor_j, melhor_tamanho


def blocos_correspondentes(a, b, offset_a=0, offset_b=0):
    """Passo 3: recursão — acha o match, depois recursa antes e depois dele."""
    if not a or not b:
        return []

    b2j = construir_hash(b)
    i, j, tamanho = encontrar_maior_match(a, b, b2j)

    if tamanho == 0:
        return []

    # recursão no pedaço ANTES do match
    antes = blocos_correspondentes(
        a[:i], b[:j], offset_a, offset_b
    )

    bloco_atual = (offset_a + i, offset_b + j, tamanho)

    # recursão no pedaço DEPOIS do match
    depois = blocos_correspondentes(
        a[i + tamanho:], b[j + tamanho:],
        offset_a + i + tamanho, offset_b + j + tamanho
    )

    return antes + [bloco_atual] + depois


def mostrar_resultado(a, b, blocos):
    print(f"a = {a!r}")
    print(f"b = {b!r}\n")
    for pos_a, pos_b, tamanho in blocos:
        trecho = a[pos_a:pos_a + tamanho]
        print(f"  match {trecho!r:>8}  (a[{pos_a}:{pos_a + tamanho}] == b[{pos_b}:{pos_b + tamanho}])")


if __name__ == "__main__":
    a = "ABCXYZ"
    b = "ABCPQZ"

    blocos = blocos_correspondentes(a, b)
    mostrar_resultado(a, b, blocos)

    print("\n--- comparando com o difflib real ---\n")

    import difflib
    sm = difflib.SequenceMatcher(None, a, b)
    for match in sm.get_matching_blocks():
        if match.size:
            print(f"  match {a[match.a:match.a + match.size]!r:>8}  "
                  f"(a[{match.a}:{match.a + match.size}] == b[{match.b}:{match.b + match.size}])")
