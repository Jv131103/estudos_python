"""
Elabore um programa para calcular a hipotenusa de um triângulo.

Dicas:

    Veja o módulo math (math.hypot);

    Utilize a seguinte fórmula: hipotenusa=(a²+b²)¹/2:

"""
a = float(input("a: "))  # cateto adjascente
b = float(input("b: "))  # cateto oposto

# modelo 1
import math

print(math.hypot(a, b))

hipotenusa = (a**2 + b**2)**(1 / 2)
print(hipotenusa)
