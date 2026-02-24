import timeit
from random import choice, randint

from main import compactar, compactar2

alfabeto = "abcdefghijklmnopqrstuvwxyz"
limite = 100_000
teste = "".join([choice(alfabeto) * randint(1, 100) for i in range(0, limite)])

testes = {
    "compactar_v1": compactar,
    "compactar_v2": compactar2
}

for nome, func in testes.items():
    tempo = timeit.timeit(lambda: func(teste), number=3)
    print(f"{nome:25}: {tempo:.4f} segundos")
