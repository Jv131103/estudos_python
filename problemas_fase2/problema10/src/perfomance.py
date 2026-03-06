import timeit

from main import (gerar_lista_inplace, gerar_lista_nao_inplace,
                  gerar_lista_nao_inplace2, posicao_circular_ifversion,
                  posicao_circular_mathversion, posicao_circular_ternario,
                  posicao_circular_try, posicao_circular_whileversion)


def benchmark(func, repeat=5, number=1000):
    tempos = timeit.repeat(func, repeat=repeat, number=number)
    return min(tempos)


def main():
    lista = list(range(1000))

    posicoes = [
        ("math", posicao_circular_mathversion),
        ("if", posicao_circular_ifversion),
        ("while", posicao_circular_whileversion),
        ("ternario", posicao_circular_ternario),
        ("try", posicao_circular_try),
    ]

    geradores = [
        ("inplace", gerar_lista_inplace),
        ("nao_inplace", gerar_lista_nao_inplace),
        ("nao_inplace2", gerar_lista_nao_inplace2),
    ]

    for nome_gerador, func_gerador in geradores:
        print(f"\n=== {nome_gerador} ===")

        for nome_posicao, func_posicao in posicoes:
            if nome_gerador == "inplace":
                teste = lambda fg=func_gerador, fp=func_posicao: fg(lista.copy(), fp)
            else:
                teste = lambda fg=func_gerador, fp=func_posicao: fg(lista, fp)

            tempo = benchmark(teste)
            print(f"{nome_posicao:10} : {tempo:.6f} s")


if __name__ == "__main__":
    main()
