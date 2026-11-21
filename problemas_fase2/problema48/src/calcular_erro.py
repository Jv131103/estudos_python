def calcular_erro(real, previsto):
    diferenca = real - previsto
    erro = diferenca**2
    return diferenca, erro


if __name__ == "__main__":
    print("==" * 20)
    print("TESTANDO ERRO QUADRÁTICO")
    print("==" * 20)
    testes = [
        (40, 35, 5, 25),
        (50, 45, 5, 25),
        (95, 85, 10, 100)
    ]
    for real, previsao, diferenca_esperada, erro_quadratico_esperado in testes:
        passou = "FALHA"
        diferenca_retornada, erro_quadratico_retornado = calcular_erro(real, previsao)

        esperado = diferenca_retornada == diferenca_esperada and erro_quadratico_retornado == erro_quadratico_esperado

        if esperado:
            passou = "OK"

        print(f"{passou}! Valores {real, previsao, diferenca_esperada, erro_quadratico_esperado}")
        print("DIFERENCA:")
        print(f"\tDIFERENCA ESPERADA: {diferenca_esperada}")
        print(f"\tDIFERENCA RETORNADA: {diferenca_retornada}")
        print("ERRO QUADRÁTICO:")
        print(f"\tERRO ESPERADO: {erro_quadratico_esperado}")
        print(f"\tERRO RETORNADO: {erro_quadratico_retornado}")
        print("--" * 20)
