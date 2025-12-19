import string


def valida(senha, case="mai"):
    cases = {
        "mai": string.ascii_uppercase,
        "num": string.digits,
        "min": string.ascii_lowercase,
        "esp": string.punctuation
    }
    for valor in senha:
        if valor in cases[case]:
            return True
    return False


def senha_valida(senha):
    if len(senha) < 8:
        print("A senha precisa conter ao menos 8 caracteres")
        return False

    # Validar se existe uma maiúscula
    if not valida(senha, case="mai"):
        print("Senha precisa ao menos obter um dado maiúsculo")
        return False

    # Validar se existe uma minúsculas
    if not valida(senha, case="min"):
        print("A senha precisa conter ao menos um dado minúsculos")
        return False

    # Validar se existe ao menos um numero
    if not valida(senha, case="num"):
        print("A senha precisa conter ao menos 1 caractere numérico")
        return False

    # Valida se existe um caractere especial
    if not valida(senha, case="esp"):
        print("A senha precisa conter ao menos 1 caractere especial")
        return False

    print("Senha Válida")
    return True


print(senha_valida("Abc@123e"))
print(senha_valida("@abC12355"))
