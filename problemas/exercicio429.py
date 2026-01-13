"""
Faça um programa que:

Leia:

    idade

    se é estudante (True/False)

    se tem documento (True/False)

Verifique se pode entrar:

    idade ≥ 18 e tem documento

    ou é estudante

Use parênteses corretamente.
"""

idade = int(input("Idade: "))

estudante = input("É estudante? [y / n] ").lower()
eh_estudante = estudante == 'y'

documento = input("Têm documento? [y / n] ").lower()
tem_doc = documento == 'y'

pode_entrar = (idade >= 18 and tem_doc) or eh_estudante
print(pode_entrar)
