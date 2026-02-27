import timeit
from random import randint

from main import segundo_maior, segundo_maior_ordenado, segundo_maior_ordenado2

functions = {
    "segundo_maior_manual": segundo_maior,
    "segundo_maior_ordenado": segundo_maior_ordenado,
    "segundo_maior_ordenado_in_place": segundo_maior_ordenado2
}

limite = 100_000
lista_desordenada = [randint(0, 100_000) for _ in range(limite)]

for nome, func in functions.items():
    tempo = timeit.timeit(
        lambda f=func, base=lista_desordenada: f(base.copy()),
        number=3
    )
    print(f"{nome:25}: {tempo:.4f} segundos")
