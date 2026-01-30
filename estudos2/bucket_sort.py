def bucket_sort(lista):
    if not lista:
        return []

    valor_maximo = max(lista)

    # número de buckets por dezenas
    qtd_buckets = valor_maximo // 10 + 1

    # cria buckets
    buckets = [[] for _ in range(qtd_buckets)]

    # distribui
    for valor in lista:
        idx = valor // 10
        buckets[idx].append(valor)

    # ordena cada bucket (insertion sort simples)
    for bucket in buckets:
        for i in range(1, len(bucket)):
            atual = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > atual:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = atual

    # concatena
    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)

    return resultado


print(bucket_sort([42, 32, 23, 52, 25, 47]))
