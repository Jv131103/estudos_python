"""
Um grande cliente seu sofreu um ataque hacker: o servidor foi sequestrado
por um software malicioso que criptografou todos os discos e solicita a
digitação de uma senha para a liberação da máquina. E é claro que os
criminosos exigem um pagamento para informar a senha.

Ao analisar o código do programa deles, você descobre que a senha é
composta pela palavra “LIBERDADE” seguida do fatorial dos minutos que
a máquina estiver marcando no momento da digitação da senha (se a máquina
estiver marcando 5 minutos, a senha será LIBERDADE120). Como solução, você
deverá desenvolver um programa que receba do usuário os minutos atuais e
exiba na tela a senha necessária para desbloqueio. Atenção: seu programa
não pode utilizar funções prontas para o cálculo do fatorial. Ele deve
obrigatoriamente utilizar loop.
"""


def fatorial(minutos):
    if minutos < 0:
        raise ValueError("minutos precisa ser >= 0")

    if minutos == 0:
        return 1

    mult = 1

    for num in range(minutos, 0, -1):
        mult *= num

    return mult


def fatorial_recursivo(n):
    if n < 0:
        raise ValueError("n deve ser >= 0")
    if n == 0:
        return 1
    return n * fatorial_recursivo(n - 1)


def liberar_criptografia(fatorial):
    return f"LIBERDADE{fatorial}"


try:
    minutos = int(input("Digite os minutos atuais: "))
    senha = liberar_criptografia(fatorial(minutos))
    print("Senha:", senha)
except ValueError:
    print("Digite apenas números inteiros.")
