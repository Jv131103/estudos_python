def max_window(lista, k):
    resultado = []

    for i in range(len(lista) - k + 1):
        janela = []

        for j in range(i, i + k):
            janela.append(lista[j])

        resultado.append(max(janela))

    return resultado


def max_window2(nums, k):

    resultado = []

    for i in range(len(nums) - k + 1):

        janela = nums[i: i + k]

        resultado.append(max(janela))

    return resultado


maiores = max_window([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(maiores)

maiores = max_window2([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(maiores)
