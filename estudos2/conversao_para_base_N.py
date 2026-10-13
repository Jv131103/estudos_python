import string


def decimal_para_base(numero, base):
    if base < 2 or base > 36:
        raise ValueError("A base deve estar entre 2 e 36.")

    if numero == 0:
        return "0"

    negativo = numero < 0
    numero = abs(numero)

    digitos = {}
    if base > 10:
        inicio = 10
        letra = 0
        while inicio != base:
            digitos[str(inicio)] = string.ascii_uppercase[letra]
            letra += 1
            inicio += 1

    lista = []
    while numero > 0:
        resto = numero % base
        lista.append(str(resto))
        numero //= base

    lista = lista[::-1]
    for i in range(len(lista)):
        lista[i] = digitos.get(lista[i], lista[i])

    resultado = "".join(lista)

    if negativo:
        resultado = "-" + resultado

    return resultado


def base_para_decimal(numero, base):
    if base < 2 or base > 36:
        raise ValueError("A base deve estar entre 2 e 36.")

    if numero == 0:
        return "0"

    decimal = 0
    potencia = 0

    for caractere in reversed(numero):
        # Converte '0'-'9' e 'A'-'F' (ou 'a'-'f') para seu valor de 0 a 15
        if '0' <= caractere <= '9':
            digito = int(caractere)
        else:
            # 'A' vira 10, 'B' vira 11, ..., 'F' vira 15
            digito = ord(caractere.upper()) - ord('A') + 10

        # Aplica a fórmula com a base N
        decimal += digito * (base ** potencia)
        potencia += 1

    return decimal


print(decimal_para_base(10, 2))
print(decimal_para_base(25, 8))
print(decimal_para_base(255, 16))
print(decimal_para_base(100, 3))
print(decimal_para_base(123, 20))
print(decimal_para_base(0, 2))
print(decimal_para_base(-25, 2))
print()
print(base_para_decimal("1010", 2))
print(base_para_decimal("31", 8))
print(base_para_decimal("FF", 16))
print(base_para_decimal("10201", 3))
