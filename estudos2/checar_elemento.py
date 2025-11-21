def checar_comum(lista_1, lista_2):
    for i in lista_1:
        for j in lista_2:
            if i == j:
                return True
    return False


print(checar_comum([1, 2, 3], [4, 5, 3]))
print(checar_comum([2, 3, 3], [1, 2, 4, 5, 4]))
print(checar_comum([11, 12], [1, 0]))
