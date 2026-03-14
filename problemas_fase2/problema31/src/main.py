try:
    from .classes import Deque, Pilha
    from .funcoes import (dois_ponteiros, manual, recursicion, reverse_py,
                          slicing_py, slicing_py2, tecnica_pilha)
except (ModuleNotFoundError, ImportError):
    from classes import Deque, Pilha
    from funcoes import (dois_ponteiros, manual, recursicion, reverse_py,
                         slicing_py, slicing_py2, tecnica_pilha)


def is_palinder_deque(string):
    d = Deque()

    for char in string:
        d.append_left(char)

    return "".join(d.dados) == string


def is_palinder_class_pilha(string):
    p = Pilha()

    for char in string:
        p.push(char)

    inverso = []

    while not p.is_empty():
        inverso.append(p.pop())

    return "".join(inverso) == string


def is_palinder_list_pilha(string):
    return tecnica_pilha(string) == string


def is_palinder_slicing1(string):
    return slicing_py(string) == string


def is_palinder_slicing2(string):
    return slicing_py2(string) == string


def is_palinder_dois_ponteiros(string):
    return dois_ponteiros(string) == string


def is_palinder_manual(string):
    return manual(string) == string


def is_palinder_reverse(string):
    return reverse_py(string) == string


def is_palinder_recursicion(string):
    return recursicion(string) == string


if __name__ == "__main__":
    valor = "banana"

    print(is_palinder_deque(valor))
    print(is_palinder_class_pilha(valor))
    print(is_palinder_list_pilha(valor))
    print(is_palinder_dois_ponteiros(valor))
    print(is_palinder_slicing1(valor))
    print(is_palinder_slicing2(valor))
    print(is_palinder_manual(valor))
    print(is_palinder_reverse(valor))
    print(is_palinder_recursicion(valor))
