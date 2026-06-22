def is_perfect(number):
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("Número, precisa ser do tipo inteiro")
    elif 0 <= number <= 1 :
        return False
    elif number < 0:
        number = abs(number)

    soma = 0
    for valor in range(1, number):
        if number % valor == 0:
            soma += valor

    return soma == number


def is_perfect2(number):
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError("Número, precisa ser do tipo inteiro")
    elif 0 <= number <= 1 :
        return False
    elif number < 0:
        number = abs(number)

    soma = 1
    for valor in range(2, int(number**0.5) + 1):
        if number % valor == 0:
            soma += valor
            soma += number // valor

    return soma == number


if __name__ == "__main__":
    print(is_perfect(6))
    print(is_perfect(28))
    print(is_perfect(12))
    print()
    print(is_perfect2(6))
    print(is_perfect2(28))
    print(is_perfect2(12))
