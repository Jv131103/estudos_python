def encontrar_assentos(sala):
    for indice_fileira, fileira in enumerate(sala):
        for indice_coluna in range(len(fileira) - 1):
            atual = fileira[indice_coluna]
            proximo = fileira[indice_coluna + 1]

            if atual == proximo and atual == ".":
                return indice_fileira, indice_coluna

    return None


print(encontrar_assentos(["XX.XX", "X..XX", "...X."]))
print(encontrar_assentos(["..XX", "X..X"]))
print(encontrar_assentos(["X.X", "X.X"]))
print(encontrar_assentos(["X.", ".X"]))
print(encontrar_assentos([".", ".."]))
print(encontrar_assentos([]))
print(encontrar_assentos(["", "X.."]))
print(encontrar_assentos(["XX..", "..XX"]))
