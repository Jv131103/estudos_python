def top3(valores):
    unicos = []
    for v in valores:
        if v not in unicos:
            unicos.append(v)

    unicos.sort(reverse=True)          # deveria sair decrescente
    return unicos[:3]      # isso pega os 3 menores


print(top3([5, 1, 5, 9, 2, 9, 7, 7, 3]))
