def calculadora():
    soma = lambda x, y: x + y
    subtracao = lambda x, y: x - y
    multiplicacao = lambda x, y: x * y
    divisao = lambda x, y: x / y
    return soma, subtracao, multiplicacao, divisao


soma, sub, mult, div = calculadora()

print(soma(2, 2))
print(sub(2, 2))
print(mult(2, 2))
print(div(2, 2))
