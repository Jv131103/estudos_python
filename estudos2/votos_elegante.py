MEMBROS = 5
VALIDAS = {"PLAYSTATION", "XBOX", "NINTENDO"}


def contar_votos(votos):
    contagem = {}
    for v in votos:
        contagem[v] = contagem.get(v, 0) + 1
    return contagem


def vencedor(contagem):
    # pega o maior número de votos
    maior = max(contagem.values())
    empatados = [k for k, v in contagem.items() if v == maior]
    return empatados, maior


def iniciar_votos(opcoes_validas):
    votos = []
    i = 1
    print(f"As opções são: {', '.join(sorted(opcoes_validas))}")
    print("--" * 30)

    while i <= MEMBROS:
        voto = input(f"Voto do usuário {i}: ").upper().strip()
        if voto not in opcoes_validas:
            print("Voto inválido!")
            continue
        votos.append(voto)
        i += 1

    contagem = contar_votos(votos)
    empatados, maior = vencedor(contagem)

    print("**" * 30)
    print("FIM DA VOTAÇÃO!")
    print("++" * 30)

    if len(empatados) == 1:
        print(f"Vencedor: {empatados[0]} com {maior} votos")
        return

    print(f"Empate entre: {', '.join(empatados)} com {maior} votos")
    print("Vamos para o 2º turno (apenas entre os empatados)!")
    iniciar_votos(set(empatados))


if __name__ == "__main__":
    print("==" * 30)
    print("-- ESCOLHER UM CONSOLE ---")
    print("==" * 30)
    iniciar_votos(VALIDAS)
    print("++" * 30)
