from datetime import date

contatos = []  # lista global de contatos


def adicionar_contato():
    print('\tAdicionar contato')
    email = input('Digite o E-mail: ').strip().lower()

    # Verifica se já existe contato com esse e-mail
    if contatos:
        for contato in contatos:
            if email == contato['email']:
                print('Este contato já existe.')
                return

    nome = input('Nome: ').strip().title()
    sobrenome = input('Sobrenome: ').strip().title()
    telefone = input('Telefone: ').strip()

    contatos.append({
        'email': email,
        'nome': nome,
        'sobrenome': sobrenome,
        'telefone': telefone,
        'data': date.today().strftime('%d/%m/%Y')
    })

    print('Contato adicionado com sucesso!')


def alterar_contato():
    if contatos:
        email = input('Digite o e-mail do contato que deseja alterar: ').strip().lower()
        for contato in contatos:
            if contato['email'] == email:
                print(f"Nome do contato: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
                print('1 - Alterar nome')
                print('2 - Alterar telefone')
                print('3 - Voltar')
                escolha = input('>> ').strip()

                if escolha == '1':
                    novo_nome = input('Digite um novo nome para o contato: ').strip().title()
                    contato['nome'] = novo_nome
                    print('Nome alterado com sucesso!')
                    return

                elif escolha == '2':
                    novo_tel = input('Digite um novo telefone para o contato: ').strip()
                    contato['telefone'] = novo_tel
                    print('Telefone alterado com sucesso!')
                    return

                elif escolha == '3':
                    return

                else:
                    print('Opção inválida.')
                    return

        print('Não existe usuário cadastrado com o e-mail informado.')
    else:
        print('Não há contatos registrados na agenda.')


def procurar_contato():
    if contatos:
        email = input('Digite o e-mail do contato: ').strip().lower()
        for contato in contatos:
            if contato['email'] == email:
                print(f"Nome: {contato['nome']} {contato['sobrenome']}")
                print(f"Telefone: {contato['telefone']}")
                print(f"Data de registro: {contato['data']}")
                return
        # Se não passou no return, não encontrou
        print('Contato não encontrado.')
    else:
        print('Não há contatos registrados na agenda.')


def remover_contato():
    if contatos:
        email = input('Digite o e-mail do contato que deseja remover: ').strip().lower()
        x = 0
        while x < len(contatos):
            if contatos[x]['email'] == email:
                contatos.pop(x)
                print('Contato removido com sucesso!')
                return
            x += 1

        print('Contato não encontrado.')
    else:
        print('Não há contatos registrados na agenda.')


def ver_contatos():
    if contatos:
        contatos_ordenados = sorted(
            contatos,
            key=lambda contato: contato['nome'] + ' ' + contato['sobrenome']
        )
        for indice, contato in enumerate(contatos_ordenados, start=1):
            print(f' Contato {indice} '.center(50, '-'))
            print(f"Nome: {contato['nome']} {contato['sobrenome']}")
            print(f"E-mail: {contato['email']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Data de registro: {contato['data']}")
            print()
    else:
        print('Não há contatos registrados na agenda.')


def menu():
    print(' Programa Agenda '.center(50, '='))
    print('\t1 - Adicionar contato')
    print('\t2 - Alterar contato')
    print('\t3 - Procurar contato')
    print('\t4 - Remover contato')
    print('\t5 - Ver contatos')
    print('\t6 - Sair')


def main():
    escolha = ''
    while escolha != '6':
        menu()
        escolha = input('>> ').strip()

        if escolha == '1':
            adicionar_contato()

        elif escolha == '2':
            alterar_contato()

        elif escolha == '3':
            procurar_contato()

        elif escolha == '4':
            remover_contato()

        elif escolha == '5':
            ver_contatos()

        elif escolha == '6':
            print('Fim do Programa.')
        else:
            print('Escolha inválida.')


if __name__ == '__main__':
    main()
