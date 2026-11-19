def localizar_tesouro(mapa):
    for indice_fileira, fileira in enumerate(mapa):
        for indice_coluna in range(len(fileira)):
            atual = fileira[indice_coluna]

            if atual == "T":
                print("TESOURO")
                return indice_fileira, indice_coluna
            elif atual == "X":
                print("Obstáculo")
            elif atual == ".":
                print("Água")

    print("SEM TESOURO")
    return None


print(localizar_tesouro(["..X..", ".X.T.", "X...."]))
print()
print(localizar_tesouro(["T...", "...."]))
print()
print(localizar_tesouro(["....", "...T"]))
print()
print(localizar_tesouro([".X.", "X.X"]))
print()
print(localizar_tesouro([]))
print()
print("6")
print(localizar_tesouro(["", "X.T"]))
print()
print(localizar_tesouro(["..T.", "T..."]))
