def plus_one(digits):
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0

    return [1] + digits


def plus_one_com_carry(digits):
    carry = 1

    for i in range(len(digits) - 1, -1, -1):
        soma = digits[i] + carry

        digits[i] = soma % 10
        carry = soma // 10

        if carry == 0:
            break

    if carry:
        digits.insert(0, carry)

    return digits


print(plus_one([9, 9, 9]))
print(plus_one([1, 2, 3]))
print(plus_one([1, 2, 9]))
print(plus_one([4, 5, 0]))
print()
print(plus_one_com_carry([9, 9, 9]))
print(plus_one_com_carry([1, 2, 3]))
print(plus_one_com_carry([1, 2, 9]))
print(plus_one_com_carry([4, 5, 0]))
