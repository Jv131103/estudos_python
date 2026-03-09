def insertion_sort_intervalo(lista, inicio, fim):
    for i in range(inicio + 1, fim):
        chave = lista[i]
        j = i - 1

        while j >= inicio and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave


def merge(lista, inicio1, fim1, inicio2, fim2):
    esquerda = lista[inicio1:fim1]
    direita = lista[inicio2:fim2]

    i = 0
    j = 0
    k = inicio1

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1
        k += 1

    while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        k += 1

    while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1


def calcular_minrun(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r


def contar_run(lista, inicio):
    n = len(lista)

    if inicio >= n - 1:
        return 1

    fim = inicio + 1

    if lista[fim] < lista[inicio]:
        while fim < n and lista[fim] < lista[fim - 1]:
            fim += 1
        lista[inicio:fim] = reversed(lista[inicio:fim])
    else:
        while fim < n and lista[fim] >= lista[fim - 1]:
            fim += 1

    return fim - inicio


def timsort_manual(lista):
    n = len(lista)
    if n < 2:
        return lista

    minrun = calcular_minrun(n)
    runs = []
    i = 0

    while i < n:
        run_len = contar_run(lista, i)

        if run_len < minrun:
            fim = min(i + minrun, n)
            insertion_sort_intervalo(lista, i, fim)
            run_len = fim - i

        runs.append((i, run_len))
        i += run_len

    while len(runs) > 1:
        novas_runs = []

        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                inicio1, tam1 = runs[i]
                inicio2, tam2 = runs[i + 1]

                merge(
                    lista,
                    inicio1, inicio1 + tam1,
                    inicio2, inicio2 + tam2
                )

                novas_runs.append((inicio1, tam1 + tam2))
            else:
                novas_runs.append(runs[i])

        runs = novas_runs

    return lista


lista = [5, 21, 7, 23, 19, 3, 8, 1, 2, 100, 54, 33]
print(timsort_manual(lista))
