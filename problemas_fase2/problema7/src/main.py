def busca_binaria(lista, valor):
    lista_ordenada = sorted(lista)

    esquerda = 0
    direita = len(lista_ordenada) - 1

    while esquerda <= direita:
        meio = (direita + esquerda) // 2
        if valor == lista_ordenada[meio]:
            return meio
        elif lista_ordenada[meio] > valor:
            direita = meio - 1
        elif lista_ordenada[meio] < valor:
            esquerda = meio + 1

    return -1


def busca_binaria_recursivo(lista, valor, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == valor:
        return meio
    elif lista[meio] < valor:
        return busca_binaria_recursivo(lista, valor, meio + 1, fim)
    else:
        return busca_binaria_recursivo(lista, valor, inicio, meio - 1)


if __name__ == "__main__":
    print(busca_binaria([1, 3, 5, 7, 9, 11, 13], 9))
    print(busca_binaria_recursivo([1, 3, 5, 7, 9, 11, 13], 9))
