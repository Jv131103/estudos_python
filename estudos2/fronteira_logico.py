def classificar_temperatura(graus):
    if not isinstance(graus, (int, float)) or isinstance(graus, bool):
        print("Parâmetro 'graus' precisa ser do tipo Float / Int!")
        return "Erro"

    if graus == 0:
        return "Zero absoluto"

    tabela = [
        [float("-inf"), -5, "Congelante"],
        [-6, 10, "Frio"],
        [11, 25, "Ameno"],
        [26, 35, "Quente"],
        [36, float("inf"), "Escaldante"],
    ]

    for temp1, temp2, result in tabela:
        if temp1 <= graus <= temp2:
            return result
    else:
        print(f"AVISO: {graus} não se encaixou em nenhuma faixa!")

    return ""


errors = 0
sucess = 0
temperaturas = [
    (-1, "Frio"),
    (-5, "Congelante"),
    (-6, "Congelante"),
    (-9.2, "Congelante"),
    (-10, "Congelante"),
    (0, "Zero absoluto"),
    (1, "Frio"),
    (5, "Frio"),
    (7, "Frio"),
    (10, "Frio"),
    (20, "Ameno"),
    (23.4, "Ameno"),
    (25, "Ameno"),
    (26, "Quente"),
    (30, "Quente"),
    (32, "Quente"),
    (34.65, "Quente"),
    (35, "Quente"),
    (36, "Escaldante"),
    (37, "Escaldante"),
    (40, "Escaldante"),
    (90, "Escaldante"),
    (True, "Erro"),
    (None, "Erro"),
    ("Python", "Erro")
]

for temperatura, esperado in temperaturas:
    result = classificar_temperatura(temperatura)
    assert result == esperado, f"Temperatura: {temperatura}\nRetornado na função: {result}\nEsperado: {esperado}"
