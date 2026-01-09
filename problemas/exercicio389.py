USERS = {
    "renato": "1234",
    "admin": "admin"
}

tentativas = 3

while tentativas > 0:
    user = input("Usuario: ")
    pwd = input("Senha: ")

    if user in USERS and USERS[user] == pwd:
        if user == "admin" and pwd == "admin":
            print("Senha insegura. Acesso bloqueado.")
            break
        print("Acesso liberado")
        break
    else:
        print("Acesso negado")
        tentativas -= 1
else:
    print("Acesso bloqueado por excesso de tentativas")
