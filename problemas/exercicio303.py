def comprimir(nums):
    novo = []

    filtro = []
    for valor in nums:
        if valor not in filtro:
            filtro.append(valor)

    for valor in filtro:  # Filtra e remove repetidos
        cont = 0
        numero = valor

        for num in nums:  # Aqui, faz a contagem
            if num == numero:
                cont += 1

        novo.append((numero, cont))

    return novo


valor = comprimir([1, 1, 1, 2, 2, 3])
print(valor)
