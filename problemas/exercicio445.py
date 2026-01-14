"""
Leia idade (int) e nome (str). Verifique (com uma única expressão) se:

    o nome contém a letra "a" e

    (idade é entre 18 e 65 ou idade é 16/17)

    Imprima True/False.

Use in, comparações encadeadas e parênteses.
"""

idade = int(input("Idade: "))
nome = input("Nome: ")

verificacao = 'a' in nome and ((18 <= idade <= 65) or (16 <= idade < 18))

print(verificacao)
