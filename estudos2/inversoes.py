def slicing_py(string):
    return "".join(list(string)[::-1])


def slicing_py2(string):
    return string[::-1]


def manual(string):
    lista = []

    for char in range(len(string) - 1, -1, -1):
        lista.append(string[char])

    return "".join(lista)


def dois_ponteiros(string):
    lista = list(string)

    i = 0
    j = len(lista) - 1

    while i < j:
        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1

    return "".join(lista)


def reverse_py(string):
    return "".join(reversed(string))


def tecnica_pilha(string):
    pilha = []

    for char in string:
        pilha.append(char)

    inverso = []

    while pilha:
        inverso.append(pilha.pop())

    return "".join(inverso)


def recursicion(string):
    if len(string) == 0:
        return string
    return recursicion(string[1:]) + string[0]


texto = "Python"
print(slicing_py(texto))
print(slicing_py2(texto))
print(manual(texto))
print(dois_ponteiros(texto))
print(reverse_py(texto))
print(tecnica_pilha(texto))
print(recursicion(texto))
