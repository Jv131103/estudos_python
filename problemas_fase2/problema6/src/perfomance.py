import timeit
from random import randint

from main import remover_duplicatas_inplace, remover_duplicatas_inplace2

functions = {
    "remover_duplicatas_in_place": remover_duplicatas_inplace,
    "remover_duplicatas_in_place2": remover_duplicatas_inplace2
}

limite = 10_000
lista_desordenada = [randint(0, limite) for _ in range(limite)]

for nome, func in functions.items():
    tempo = timeit.timeit(
        lambda f=func, base=lista_desordenada: f(base.copy()),
        number=3
    )
    print(f"{nome:25}: {tempo:.4f} segundos")
