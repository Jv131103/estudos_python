"""
Faça um programa que:

    Receba uma string

    Procure um número dentro dela (pode ser regex ou find)

    Se encontrar:

        use walrus para guardar o resultado

        use esse resultado dentro do bloco if

    Caso contrário, não faça nada
"""

valor = input("Digite algo: ")
numero_a_procurar = input("NÚMERO A PROCURAR: ")

if (temp := valor.find(numero_a_procurar)) > -1:
    print(f"Encontrado no índice: {temp}")
    print(f"COMPROVANDO: {valor[temp]}")
