def is_multiple(value, number):
    if number == 0:
        return None
    return value % number == 0


print(is_multiple(10, 2))
print(is_multiple(10, 3))
