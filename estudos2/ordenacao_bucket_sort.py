def bucket_sort(arr):

    if not arr:
        return arr

    n = len(arr)

    menor = min(arr)
    maior = max(arr)

    intervalo = (maior - menor) / n + 1e-9

    buckets = [[] for _ in range(n)]

    for valor in arr:
        indice = int((valor - menor) / intervalo)
        buckets[indice].append(valor)

    for bucket in buckets:
        bucket.sort()

    resultado = []

    for bucket in buckets:
        resultado.extend(bucket)

    return resultado


lista = [10, 5, 67, 0, 12, 55]
print(bucket_sort(lista))
