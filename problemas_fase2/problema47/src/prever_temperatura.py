def prever_temperatura(cpu, peso, bias):
    return peso * cpu + bias


if __name__ == "__main__":
    print("==" * 20)
    print("TESTES DE PREDICAO DE TEMPERATURA")
    testes_temps = (
        [50, 0.1, 30, 35],
        [100, 0.1, 30, 40],
        [0, 0.1, 30, 30]
    )
    print("==" * 20)
    for cpu, peso, bias, esperado in testes_temps:
        result = prever_temperatura(cpu, peso, bias)
        saida = result == esperado
        if saida:
            print(f"OK!\nVALORES: {cpu, peso, bias}\n\tESPERADO: {esperado}\n\tRETORNADO: {result}")
        else:
            print(f"FALHA!\nVALORES: {cpu, peso, bias}\n\tESPERADO: {esperado}\n\tRETORNADO: {result}")
        print("--" * 20)
