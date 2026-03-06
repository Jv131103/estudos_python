import timeit

from main import circularizar, circularizar2, circularizar3

lista = list(range(1000))
k = 500
repeticoes = 1_000_000

testes = [
    ("modulo", lambda: circularizar(lista, k)),
    ("if", lambda: circularizar2(lista, k)),
    ("while", lambda: circularizar3(lista, k)),
]

for nome, func in testes:
    tempo = timeit.timeit(func, number=repeticoes)
    print(f"{nome:10} : {tempo:.6f} s")
