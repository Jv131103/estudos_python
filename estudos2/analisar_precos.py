def analisar_precos(precos):
    i = 1
    altas = 0
    quedas = 0
    estaveis = 0
    total_altas = 0
    maior_alta = 0
    dias_queda = []

    while i < len(precos):
        diferenca = precos[i] - precos[i - 1]
        if diferenca > 0:
            altas += 1
            total_altas += diferenca

            if diferenca > maior_alta:
                maior_alta = diferenca

        elif diferenca < 0:
            quedas += 1
            dias_queda.append(i)

        else:
            estaveis += 1

        i += 1

    return {
        "altas": altas,
        "quedas": quedas,
        "estaveis": estaveis,
        "total_altas": total_altas,
        "maior_alta": maior_alta,
        "dias_queda": dias_queda
    }


precos = [100, 110, 105, 105, 120, 115]
print(analisar_precos(precos))
