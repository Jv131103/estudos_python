import timeit

from main import (rotacionar, rotacionar2, rotacionar3, rotacionar4,
                  rotacionar5, rotacionar6, rotacionar7)


def medir(func, repeticoes=200):
    tempos = timeit.repeat(func, number=repeticoes, repeat=5)
    return min(tempos)


def benchmark():
    lista = list(range(1000))
    k = 200

    testes = [
        ("slicing", lambda: rotacionar(lista.copy(), k)),
        ("shift", lambda: rotacionar2(lista.copy(), k)),
        ("auxiliar", lambda: rotacionar3(lista.copy(), k)),
        ("reverse", lambda: rotacionar4(lista.copy(), k)),
        ("comprehension", lambda: rotacionar5(lista.copy(), k)),
        ("pop_insert", lambda: rotacionar6(lista.copy(), k)),
        ("duplicada", lambda: rotacionar7(lista.copy(), k)),
    ]

    for nome, func in testes:
        tempo = medir(func)
        print(f"{nome:15} : {tempo:.6f} s")


if __name__ == "__main__":
    benchmark()
