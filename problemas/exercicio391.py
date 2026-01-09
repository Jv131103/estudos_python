nota = int(input())

resultados = {
    10: "Perfeito",
    9: "Otimo",
    8: "Bom",
    7: "Regular"
}

if not 0 <= nota <= 10:
    print("Nota inválida!")
else:
    print(resultados.get(nota, "Precisa melhorar"))
