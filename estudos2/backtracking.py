def gerar_subconjuntos(nums):
    resultado = []
    caminho = []

    def backtrack(i):
        if i == len(nums):
            resultado.append(caminho.copy())
            return

        caminho.append(nums[i])
        backtrack(i + 1)

        caminho.pop()
        backtrack(i + 1)

    backtrack(0)
    return resultado


print(gerar_subconjuntos([1, 2, 3, 4, 5]))
