def analisar_email(email):
    indice_arroba = email.find("@")
    if indice_arroba == -1:
        print("Email inválido")
        return

    username = email[:indice_arroba]
    dominio = email[indice_arroba + 1:]

    dominio_termina_com_dot_com = email.endswith('.com')

    qtd_caracteres = len(email)

    print(f"Usuário: {username}")
    print(f"Dominio: {dominio}")
    print(f"Termina com .com: {dominio_termina_com_dot_com}")
    print(f"Quantidade de caracteres: {qtd_caracteres}")


analisar_email("joao.justino@gmail.com")
