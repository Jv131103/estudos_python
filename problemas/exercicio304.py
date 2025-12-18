def data_valida(dia, mes, ano):
    if ano <= 0:
        return False

    if mes == 2 and 1 <= dia <= 28:
        return True
    elif mes in [4, 6, 9, 11] and 1 <= dia <= 30:
        return True
    elif mes in [1, 3, 5, 7, 8, 10, 12] and 1 <= dia <= 31:
        return True
    return False


print(data_valida(25, 1, 2025))
print(data_valida(28, 2, 2025))
print(data_valida(30, 2, 2025))
print(data_valida(40, 1, 2025))
print(data_valida(23, 14, 2025))
print(data_valida(2, 8, 0))
