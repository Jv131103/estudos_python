"""
Faça um programa que:

    Imprima uma tabela simples:

        Nome    Idade    Cidade
        Ana     20       SP
        João    30       RJ

Use \t.
"""

lista_usuarios = []


def input_lista():
    for _ in range(2):
        lista_usuarios.append([input("Nome: "), int(input("Idade: ")), input("Cidade: ")])


def versao_com_tab():
    print("Nome\t\tIdade\t\tCidade")
    for usuario in lista_usuarios:
        nome, idade, cidade = usuario
        print(f"{nome}\t\t{idade}\t\t{cidade}")


def versao_sem_tab():
    print(f"{'Nome':<10}{'Idade':<10}{'Cidade':<10}")
    for nome, idade, cidade in lista_usuarios:
        print(f"{nome:<10}{idade:<10}{cidade:<10}")


input_lista()
versao_sem_tab()
