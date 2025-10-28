# Tipos numéricos: (int, float, complex)
x = 10  # int
y = 10.5  # float
z = 10 + 1j  # complex
print(x, type(x))
print(y, type(y))
print(z, type(z))

# Conversão (Casting)
idade = input("Idade: ")
print(idade, type(idade))
idade = int(idade)
print(idade, type(idade))

peso = float(input("Peso: "))
print(peso, type(peso))

print(int('10'))
print(str(10))

n = 10.5
n = int(n)
print(n)

print(float(198))

# Opreções aritméticas
print(10.5 + 10)  # soma (+)
print(17.2 - 5)  # subtração (-)
print(10 / 5)  # Divisão real (/) -> quociente completo
print(10 / 3)
print(10 // 3)  # Divisão inteira (//) -> apenas quociente inteiro
print(8 % 2)  # Módulo da divisão (%) -> Resto da divisão
print(2**2)  # Potência (**)
print(4**1 / 2)  # Técnica para encontrar raiz quadrada
