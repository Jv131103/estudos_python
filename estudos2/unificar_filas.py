def mesclar_pedidos(unidade_a, unidade_b):
    final = []

    i = 0  # Posição na unidade A
    j = 0  # Posição na unidade B

    while i < len(unidade_a) and j < len(unidade_b):
        # Compare unidade_a[i] com unidade_b[j]
        if unidade_a[i] < unidade_b[j]:
            final.append(unidade_a[i])
            i += 1
        else:
            final.append(unidade_b[j])
            j += 1

    final.extend(unidade_a[i:])
    final.extend(unidade_b[j:])

    return final


print(mesclar_pedidos([2, 5, 9], [1, 6, 10]))
print(mesclar_pedidos([1, 2], [3, 4, 5]))
print(mesclar_pedidos([1, 4, 4], [2, 4, 8]))
print(mesclar_pedidos([], [3, 7]))
print(mesclar_pedidos([1, 5], []))
print(mesclar_pedidos([], []))
print(mesclar_pedidos([-8, -2, 3], [-5, 0, 7]))
