import timeit
from random import randint

from main import (transposta, transposta2, transposta3, transposta4,
                  transposta5, transposta6)

FUNCOES = {
    "transposta1": transposta,
    "transposta2": transposta2,
    "transposta3_zip": transposta3,
    "transposta4_listcomp": transposta4,
    "transposta5_prealocada": transposta5,
    "transposta6_recursiva": transposta6,
}


def gerar_matriz(linhas, colunas):
    return [[randint(0, 100) for _ in range(colunas)] for _ in range(linhas)]


def bench(func, matriz, loops=10, repeat=5):
    tempos = timeit.repeat(
        lambda: func(matriz),
        number=loops,
        repeat=repeat
    )
    return min(tempos) / loops


def main():
    tamanhos = [
        (10, 10),
        (100, 100),
        (300, 300),
    ]

    for linhas, colunas in tamanhos:
        print(f"\n===== Matriz {linhas}x{colunas} =====")
        matriz = gerar_matriz(linhas, colunas)

        for nome, func in FUNCOES.items():
            try:
                tempo = bench(func, matriz)
                print(f"{nome:25}: {tempo:.6f} s/chamada")
            except RecursionError:
                print(f"{nome:25}: RecursionError")


if __name__ == "__main__":
    main()
