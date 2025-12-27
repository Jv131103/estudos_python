def agrupar_por_tamanho(frase: str, ordenar: bool = False) -> dict[int, list[str]]:
    pontuacao = ",.;:!?()[]{}\"'"

    grupos: dict[int, list[str]] = {}

    for palavra in frase.split():
        palavra_limpa = palavra.strip(pontuacao).lower()
        if not palavra_limpa:
            continue

        tamanho = len(palavra_limpa)

        if tamanho not in grupos:
            grupos[tamanho] = [palavra_limpa]
        elif palavra_limpa not in grupos[tamanho]:
            grupos[tamanho].append(palavra_limpa)

    if ordenar:
        return {k: grupos[k] for k in sorted(grupos)}

    return grupos


print(agrupar_por_tamanho("Python é uma linguagem muito poderosa"))
