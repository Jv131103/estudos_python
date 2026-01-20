# Com índices default
def soma_div(lista, ini=0, fim=None):
    if fim is None:
        fim = len(lista)  # fim exclusivo

    if ini == fim:
        return 0
    if fim - ini == 1:
        return lista[ini]

    meio = (ini + fim) // 2
    return soma_div(lista, ini, meio) + soma_div(lista, meio, fim)


# Com técnica slicing
def soma_div_conquer(lista):
    if not lista:
        return 0

    if len(lista) == 1:
        return lista[0]

    meio = len(lista) // 2

    esquerda = lista[:meio]
    direita = lista[meio:]

    return soma_div_conquer(esquerda) + soma_div_conquer(direita)


# Com índices default
def soma_rec(lista, i=0):
    if i == len(lista):
        return 0
    return lista[i] + soma_rec(lista, i + 1)


# Com técnica slicing
def soma_comum(lista):
    if not lista:
        return 0

    return lista[0] + soma_comum(lista[1:])


lista = list(range(10000))
print(soma_div(lista))
# print(soma_rec(lista))  # Nem lê por excesso de recursão
