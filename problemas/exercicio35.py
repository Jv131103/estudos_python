"""
O Índice de Massa Corporal (IMC) é utilizado para mensurar o peso ideal de uma
pessoa. Escreva um programa que peça o nome, a idade , o peso e a altura do
usuário. Ao final calcule e mostre o resultado do seu IMC e classifique este
resultado de acordo com a regra a seguir.

    IMC<17 - Muito abaixo do peso ideal

    17<=IMC<18,5 - Abaixo do peso

    18,5<=IMC<25 - Peso normal

    25<=IMC<30 - Acima do peso

    30<=IMC<35 - Obesidade I

    35<=IMC<40 - Obesidade II (severa)

    IMC>=40 - Obesidade III (mórbida)

Lembre que: IMC=massa/(altura*altura)
"""

nome = input("Nome: ")
idade = int(input("Idade: "))
peso = float(input("Peso: "))
altura = float(input("Altura: "))

IMC = peso / (altura * altura)
print(f"RESULTADOS DE IMC DE {nome} de {idade} anos:")
if IMC < 17:
    print("Muito abaixo do peso ideal")
elif IMC <= 18.5:
    print("Abaixo do peso")
elif 18.5 <= IMC < 25:
    print("Peso normal")
elif 25 <= IMC < 30:
    print("Acima do peso")
elif 30 <= IMC < 35:
    print("Obesidade I")
elif 35 <= IMC < 40:
    print("Obesidade II (severa)")
else:
    print("Obesidade III (mórbido)")
