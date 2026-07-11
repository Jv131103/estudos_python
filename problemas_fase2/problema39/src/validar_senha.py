def validar_senha(senha: str):
    if len(senha) < 8:
        return False

    dados = {
        "maiusculas": 0,
        "minusculas": 0,
        "especiais": 0,
        "numericos": 0
    }

    for char in senha:
        if char.isupper():
            dados["maiusculas"] += 1
        elif char.islower():
            dados["minusculas"] += 1
        elif char.isdigit():
            dados["numericos"] += 1
        elif char in "!@#$%^&*":
            dados["especiais"] += 1

    for value in dados.values():
        if not value:
            return False

    return True


if __name__ == "__main__":
    print(validar_senha("Abc123@a"))
    print(validar_senha("123@a"))
    print(validar_senha("123@aaaaa"))
    print(validar_senha("@Aaaaa!!"))
    print(validar_senha("123@AQAQAQ"))
    print(validar_senha("123aaAQAQAQ"))
