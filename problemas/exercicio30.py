"""
Escreva um programa que solicite o nome, o sobrenome e o salário atual de um
funcionário. Ao fim, calcule seu novo salário considerando cenários hipotéticos,
com os seguintes aumentos: 10%, 25%,30% e 50%. A mensagem na tela deverá seguir
o seguinte padrão:


    "Olá, [nome] [sobrenome]"

    "Seu salário atual é : [salário]"

    "Seu salário com 10% de aumento é: [salário]"

    "Seu salário com 25% de aumento é: [salário]"

    "Seu salário com 30% de aumento é: [salário]"

    "Seu salário com 50% de aumento é: [salário]"


No campo nome e sobrenome utilize os métodos strip() e title(). Lembre-se que o
primeiro método permite remover os espaços antes e após a string, enquanto que
o último permite colocar a string no formato titlecased (capitaliza string).
"""

nome = input("Nome: ").strip().title()
sobrenome = input("Sobrenome: ").strip().title()
salario = float(input("Salário [ATUAL]: "))

aumento10porcento = salario + (salario * 0.1)
aumento25porcento = salario + (salario * 0.25)
aumento30porcento = salario + (salario * 0.3)
aumento50porcento = salario + (salario * 0.5)

print(f"Olá, {nome} {sobrenome}")
print(f"Seu salário com 10% de aumento é: {aumento10porcento}")
print(f"Seu salário com 25% de aumento é: {aumento25porcento}")
print(f"Seu salário com 30% de aumento é: {aumento30porcento}")
print(f"Seu salário com 50% de aumento é: {aumento50porcento}")
