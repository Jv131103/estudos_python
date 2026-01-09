token = input("Token: ")

db_admins = ["ADMIN-9X2", "ADMIN-7K1"]

if token in db_admins:
    print("Acesso ADMIN liberado")
else:
    print("Acesso negado")
