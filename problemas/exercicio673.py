"""
Uma grande empresa de jogos deseja tornar seus games mais desafiadores.
Para isso, ela contratou você para desenvolver um algoritmo que será
aplicado futuramente em diversos outros games: o algoritmo da sorte de
Fibonacci.

O intuito da empresa é fazer com que se torne mais difícil os jogadores
conseguirem ter sucesso nas ações que realizam nos games. Por isso o seu
algoritmo deverá funcionar da seguinte forma: o usuário precisa digitar
um valor numérico inteiro e o algoritmo deverá verificar se esse valor
está presente na sequência de Fibonacci. Se o número estiver presente na
sequência, o algoritmo deve exibir a mensagem “Ação bem-sucedida!”, caso
contrário, deverá exibir a mensagem “A ação falhou...”.

A sequência de Fibonacci é muito simples e possui uma lógica de fácil
compreensão: ela se inicia em 1 e cada novo elemento da sequência é a soma
dos dois elementos anteriores. Portanto: 1, 1, 2, 3, 5, 8, 13, 21, e assim
por diante.

Logo, se o usuário digitar o número 55 o programa deverá informar que a ação
foi bem-sucedida, afinal 55 está entre os números da sequência.

Entretanto, se o usuário digitar o número 6, por exemplo, a ação não será
bem-sucedida, pois o número 6 não está na sequência.
"""


def number_in_fibonacci(numero):
    x = 0
    y = 1

    if numero == x or numero == y:
        return True

    cont = 0

    while cont <= numero:
        temp = x
        x = y
        y = temp + x
        if y == numero:
            return True
        cont += 1

    return False


def number_in_fibonacci_elegante(numero):
    if not numero or numero == 1:
        return True
    x = 0
    y = 1
    for _ in range(1, numero + 1):
        x, y = x + y, x
        if x == numero:
            return True
    return False


while True:
    try:
        num = int(input("Número: "))
        if number_in_fibonacci_elegante(num):
            print("Ação bem sucedida!")
            break
        print("A ação falhou...")
    except ValueError:
        print("Digite apenas números!")
