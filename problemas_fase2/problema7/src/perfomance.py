import timeit
from random import choice

from main import busca_binaria, busca_binaria_recursivo

FUNCS = {
    "binario_iterativo": busca_binaria,
    "binario_recursivo": busca_binaria_recursivo
}

simulacao = list(range(0, 1_000_000))
numero = choice(simulacao)

for nome, func in FUNCS.items():
    tempo = timeit.timeit(
        lambda: func(simulacao, numero),
        number=3
    )
    print(f"{nome:25}: {tempo:.6f} segundos")
