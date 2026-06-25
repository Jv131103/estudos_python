def tamanho_is_par(lista):
    slow = 0
    for fast in range(1, len(lista) + 1):
        slow += 1

    return fast % 2 == 0


def tamanho_is_par2(lista):
    slow = 0
    fast = 0

    while fast < len(lista):
        slow += 1
        fast += 2

    return fast == len(lista)


def tamanho_is_par3(lista):
    # Começa como True (uma lista vazia, de tamanho 0, é par)
    e_par = True

    # Percorre a lista elemento por elemento (sem usar len)
    for _ in lista:
        # A cada elemento encontrado, "viramos a chave"
        e_par = not e_par

    # O estado final da chave nos diz se o total é par ou ímpar
    return e_par


print(tamanho_is_par([1, 2, 3]))
print(tamanho_is_par([1, 2, 3, 4]))
print(tamanho_is_par([1, 2, 3, 4, 5]))
print(tamanho_is_par([1, 2, 3, 4, 5, 6]))
print()
print(tamanho_is_par2([1, 2, 3]))
print(tamanho_is_par2([1, 2, 3, 4]))
print(tamanho_is_par2([1, 2, 3, 4, 5]))
print(tamanho_is_par2([1, 2, 3, 4, 5, 6]))
print()
print(tamanho_is_par3([1, 2, 3]))
print(tamanho_is_par3([1, 2, 3, 4]))
print(tamanho_is_par3([1, 2, 3, 4, 5]))
print(tamanho_is_par3([1, 2, 3, 4, 5, 6]))
