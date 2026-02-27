"""
Hora de decidir! Os colaboradores da sua equipe foram sorteados para ganhar
um console de última geração, cada um, em razão do bom desempenho que
tiveram nos últimos projetos. Por uma questão de logística, porém, a
empresa pede que todos os cinco membros da equipe recebam o mesmo aparelho.

Crie um algoritmo em que o usuário possa digitar o voto de cada um dos
5 membros da equipe e, ao final, exiba qual foi o console escolhido e com
quantos votos.

As opções são: PLAYSTATION, XBOX e NINTENDO.
"""

MEMBROS = 5


def retornar_vencedor(votos, escolhas):
    opcoes = {}
    for v in votos:
        opcoes[v] = opcoes.get(v, 0) + 1

    # maior votação
    maior = max(opcoes.values())
    empatados_topo = [k for k, v in opcoes.items() if v == maior]

    # se só 1 tem a maior votação -> vencedor
    if len(empatados_topo) == 1:
        vencedor = empatados_topo[0]
        print(f"Vencedor: {vencedor} com {opcoes[vencedor]} votos")
        return

    # empate no topo -> elimina o menor votado e refaz
    print(f"Houve empate no topo entre: {', '.join(empatados_topo)} com {maior} votos")

    # acha o(s) menor(es) votado(s)
    menor = min(opcoes.values())
    perdedores = [k for k, v in opcoes.items() if v == menor]

    # com 5 votos e 3 opções, aqui normalmente dá 1 perdedor (ex: 2-2-1)
    # mas por segurança, se empatar também no menor, elimina 1 deles (regra simples)
    perdedor = perdedores[0]

    print(f"Eliminando o perdedor: {perdedor} com {opcoes[perdedor]} votos")
    escolhas_novas = [e for e in escolhas if e != perdedor]

    print("Criando uma nova eleição...")
    print("--" * 30)
    iniciar_votos(escolhas_novas)


def iniciar_votos(escolhas=None):
    if escolhas is None:
        escolhas = ["PLAYSTATION", "XBOX", "NINTENDO"]

    votos = []
    i = 1

    print(f"As opções são: {', '.join(escolhas)}")
    print("--" * 30)

    while i <= MEMBROS:
        opcao = input(f"Voto do usuário {i}: ").upper().strip()

        if opcao not in escolhas:
            print("Voto inválido!")
            continue

        votos.append(opcao)
        i += 1

    print("**" * 30)
    print("FIM DA VOTAÇÃO!")
    print("++" * 30)
    retornar_vencedor(votos, escolhas)


if __name__ == "__main__":
    print("==" * 30)
    print("-- ESCOLHER UM CONSOLE PARA LEVAR PARA CASA ---")
    print("==" * 30)
    iniciar_votos()
    print("++" * 30)
