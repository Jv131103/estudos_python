def decimal_para_base(numero, base):
    if base < 2 or base > 36:
        raise ValueError("A base deve estar entre 2 e 36.")

    if numero == 0:
        return "0"

    digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    negativo = numero < 0
    numero = abs(numero)

    resultado = ""

    while numero > 0:
        resto = numero % base

        resultado = digitos[resto] + resultado

        numero //= base

    if negativo:
        resultado = "-" + resultado

    return resultado


def base_para_decimal(numero, base):
    if base < 2 or base > 36:
        raise ValueError("A base deve estar entre 2 e 36.")

    # Todos os símbolos possíveis da base 2 até 36
    simbolos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Garante que o número esteja em texto e maiúsculo
    numero_str = str(numero).upper()
    decimal = 0
    potencia = 0

    # Percorre de trás para frente
    for caractere in reversed(numero_str):
        if caractere not in simbolos:
            raise ValueError(f"Caractere inválido: {caractere}")

        digito = simbolos.index(caractere)

        # Garante que o dígito não seja maior ou igual à base (ex: '8' na base 8)
        if digito >= base:
            raise ValueError(f"O dígito '{caractere}' não é válido na base {base}.")

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
