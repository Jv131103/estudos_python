def primo(numero):
    if numero == 1 or numero == 0:
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True


primos = list(
    filter(lambda numero: primo(numero), range(1, 51))
)
print(primos)
