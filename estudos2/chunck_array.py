def chunk_lista(lista, size):
    chunk = []

    for i in range(0, len(lista), size):
        chunk.append(lista[i: i + size])

    return chunk


print(chunk_lista([1, 2, 3, 4, 5, 6, 7], 3))
