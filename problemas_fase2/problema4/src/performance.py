import timeit
from random import randint

from main import maior_menor_manual  # maior_menor_recursivo
from main import (maior_menor_ordenado_inplace,
                  maior_menor_ordenado_nao_inplace,
                  maior_menor_ordenado_pythonico, maior_menor_pythonico)

limite = 100_000
lista_desordenada = [randint(0, 100_000) for _ in range(limite)]

defs = {
    "min_max_manual": maior_menor_manual,
    # "min_max_recursivo": maior_menor_recursivo,
    "min_max_ordenado(Nao_Inplace)": maior_menor_ordenado_nao_inplace,
    "min_max_pythonico": maior_menor_pythonico,
    "min_max_ordenado_pythonico(Nao_Inplace)": maior_menor_ordenado_pythonico,
    "min_max_ordenado(Inplace)": maior_menor_ordenado_inplace
}

for nome, func in defs.items():
    tempo = timeit.timeit(
        lambda f=func, base=lista_desordenada: f(base.copy()),
        number=3
    )
    print(f"{nome:25}: {tempo:.4f} segundos")
