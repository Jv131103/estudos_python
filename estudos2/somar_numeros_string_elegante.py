def somar_numeros(texto):
    soma = 0
    for palavra in texto.split():
        numero = ''.join([c for c in palavra if c.isdigit()])
        if numero:
            soma += int(numero)
    return soma


print(somar_numeros("O produto X custa 120 reais, mas com 30% de desconto fica 84."))
