def validar(senha: str):
    if len(senha) < 8:
        print("Senha precisa conter pelo menos 8 caracteres")
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

    for key, value in dados.items():
        if not value:
            print(f"Inválido! Necessário possuir caracteres {key}")
            return False

    print("Senha válida")
    return True


print(validar("Abc123@a"))
print(validar("123@a"))
print(validar("123@aaaaa"))
print(validar("@Aaaaa!!"))
print(validar("123@AQAQAQ"))
print(validar("123aaAQAQAQ"))
