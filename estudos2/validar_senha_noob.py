def validar_senha(senha):
    # 1. Verifica o tamanho primeiro (o mais fácil)
    if len(senha) < 8:
        print("Critério falhou: A senha precisa de pelo menos 8 caracteres.")
        return False

    # 2. Cria variáveis de controle (as famosas "flags") começando como Falso
    tem_maiuscula = False
    tem_numero = False
    tem_especial = False

    # 3. Olha para cada letra da senha, uma por uma
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True

        if caractere.isdigit():
            tem_numero = True

        if caractere in "!@#$%^&*":
            tem_especial = True

    # 4. Depois de olhar a senha toda, verifica o que ficou faltando
    if not tem_maiuscula:
        print("Critério falhou: A senha precisa de pelo menos uma letra maiúscula.")
        return False

    if not tem_numero:
        print("Critério falhou: A senha precisa de pelo menos um número.")
        return False

    if not tem_especial:
        print("Critério falhou: A senha precisa de pelo menos um caractere especial (!@#$%^&*).")
        return False

    # Se passou por todos os "ifs" sem dar Return False, a senha é válida!
    print("Senha válida!")
    return True
