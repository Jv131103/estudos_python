while True:
    n = int(input("Digite um número entre 0 e 10 [-1 para sair do programa]: "))
    if n == -1:
        break
    if n < 0 or n > 10:
        print("Por favor, digite um número no intervalo de 0 a 10")
