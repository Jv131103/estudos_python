import timeit

from main import is_palinder, is_palinder_tecnica_ponteiros

teste = "Socorram-me, subi no ônibus em Marrocos" * 100

funcao = {
    "is_palinder": is_palinder,
    "is_palinder_tecnica_ponteiros": is_palinder_tecnica_ponteiros
}

for nome, func in funcao.items():
    tempo = timeit.timeit(lambda: func(teste), number=3)
    print(f"{nome:25}: {tempo:.4f} segundos")
