def comprimir(nums):
    if not nums:
        return []

    novo = []
    atual = nums[0]
    cont = 1

    for x in nums[1:]:
        if x == atual:
            cont += 1
        else:
            novo.append((atual, cont))
            atual = x
            cont = 1

    novo.append((atual, cont))
    return novo


valor = comprimir([1, 1, 1, 2, 2, 3])
print(valor)
