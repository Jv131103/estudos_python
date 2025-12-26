def exibir_saldo(valor):
    notas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]

    for nota in notas:
        print(f"{valor // nota} notas de R$ {nota}")
        valor %= nota


exibir_saldo(395.30)
