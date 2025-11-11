"""
Escreva um programa que inverta uma string. Exemplos:

    Hello World!
    Python
    !dlroW olleH
    nohtyP

"""


def versao1(string):
    lista = list(string)
    lista = lista[::-1]
    return "".join(lista)


def versao2(string):
    return string[::-1]


def versao3(string):
    uniao = ""
    for char in range(len(string) - 1, -1, -1):
        uniao += string[char]
    return uniao


print(versao1("Hello World!"))
print(versao2("Hello World!"))
print(versao3("Hello World!"))
