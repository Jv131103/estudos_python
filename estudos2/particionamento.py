def particionar_lomuto(v, inicio=0, fim=None, debug=True):
    """
    Particionamento (Lomuto):
    - pivô = último elemento
    - indice_fronteira (i): marca o final da região <= pivô
    - indice_varredura (j): percorre os elementos para decidir pra que lado vão

    Retorna: índice final do pivô
    """
    if fim is None:
        fim = len(v) - 1

    pivo = v[fim]

    # i = índice de fronteira: até i, tudo é <= pivô (região "boa")
    indice_fronteira = inicio - 1

    if debug:
        print(f"\nLista inicial: {v}")
        print(f"inicio={inicio}, fim={fim}, pivo=v[{fim}]={pivo}")
        print("Regra: tudo <= pivô vai pra esquerda (até 'indice_fronteira')\n")

    # j = índice de varredura: vai varrendo do inicio até fim-1
    for indice_varredura in range(inicio, fim):
        atual = v[indice_varredura]

        if debug:
            print(f"j={indice_varredura} (varredura), atual={atual}, fronteira i={indice_fronteira}")

        # Se o elemento atual é <= pivô, ele deve ficar na região da esquerda
        if atual <= pivo:
            indice_fronteira += 1  # aumenta a região <= pivô

            # troca: coloca o atual pra dentro da região <= pivô
            v[indice_fronteira], v[indice_varredura] = v[indice_varredura], v[indice_fronteira]

            if debug:
                print(f"  atual <= pivô → i vira {indice_fronteira} e fazemos swap(i, j)")
                print(f"  lista agora: {v}")
        else:
            if debug:
                print("  atual > pivô → não mexe na fronteira, só continua")

    # No final, o pivô vai logo após a região <= pivô
    posicao_pivo = indice_fronteira + 1
    v[posicao_pivo], v[fim] = v[fim], v[posicao_pivo]

    if debug:
        print("\nFim da varredura. Colocando pivô na posição final:")
        print(f"swap(pivô em {fim}, posição_pivo em {posicao_pivo})")
        print(f"Lista final: {v}")
        print(f"Pivô {pivo} ficou no índice {posicao_pivo}\n")

    return posicao_pivo


# Demonstração:
lista = [7, 2, 1, 6, 8, 5, 3, 4]
idx = particionar_lomuto(lista, debug=True)
print("Índice retornado (pivô):", idx)
