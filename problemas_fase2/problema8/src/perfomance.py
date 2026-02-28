import timeit

from main import (inserir1, inserir2, inserir3, inserir4, inserir5, inserir6,
                  inserir7)

FUNCS = {
    "inserir_versao1": inserir1,
    "inserir_versao2": inserir2,
    "inserir_versao3": inserir3,
    "inserir_versao4": inserir4,
    "inserir_versao5": inserir5,
    "inserir_versao6": inserir6,
    "inserir_versao7": inserir7
}

CASOS = {
    "inicio": -1,
    "meio": 500_000,
    "fim": 1_000_000,
    "nao_existe": 2_000_000,
}

simulacao = list(range(0, 1_000_000))

for caso, numero in CASOS.items():
    print(f"\n=== caso: {caso} (numero={numero}) ===")
    for nome, func in FUNCS.items():
        tempos = timeit.repeat(
            stmt="func(simulacao.copy(), numero)",
            globals={"func": func, "simulacao": simulacao, "numero": numero},
            number=30,
            repeat=5
        )
        print(f"{nome:25}: {min(tempos):.6f} s (melhor de 5)")
