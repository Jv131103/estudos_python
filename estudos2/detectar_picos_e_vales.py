def analisar_picos_vales(valores):
    i = 1

    quantidade_picos = 0
    quantidade_vales = 0
    soma_picos = 0
    indices_picos = []
    indices_vales = []

    while i < len(valores) - 1:
        if valores[i] > valores[i - 1] and valores[i] > valores[i + 1]:
            quantidade_picos += 1
            indices_picos.append(i)
            soma_picos += valores[i]
        elif valores[i] < valores[i - 1] and valores[i] < valores[i + 1]:
            quantidade_vales += 1
            indices_vales.append(i)

        i += 1

    return {
        "quantidade_picos": quantidade_picos,
        "quantidade_vales": quantidade_vales,
        "soma_picos": soma_picos,
        "indices_picos": indices_picos,
        "indices_vales": indices_vales
    }


valores = [4, 7, 3, 6, 2, 8, 5]
print(analisar_picos_vales(valores))
print(analisar_picos_vales([1, 2, 3, 4, 5]))
print(analisar_picos_vales([2, 2, 2]))
print(analisar_picos_vales([5]))
