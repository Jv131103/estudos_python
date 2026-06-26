def plus_one_trace(digits):
    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        valor_original = digits[i]
        soma = valor_original + carry

        digits[i] = soma % 10
        carry = soma // 10

        if carry == 0:
            print(f"i={i}, valor={valor_original}, somou 1 e parou")
            break
        else:
            print(f"i={i}, valor={valor_original}, virou 0, carry continua")

    if carry:
        digits.insert(0, carry)

    print(f"Resultado: {digits}")
    return digits


# Testando o cenário do exercício
plus_one_trace([1, 9, 9])
