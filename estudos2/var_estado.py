campos_formulario = {
    "nome": "João Silva",
    "email": "",  # <-- Opa, o usuário esqueceu de preencher o email!
    "idade": "28"
}

formulario_valido = True  # <-- VARIÁVEL DE ESTADO (Estado inicial: Otimista)

for campo, valor in campos_formulario.items():
    if valor == "":
        formulario_valido = False  # O estado mudou e a memória da falha está salva
        break  # Não há necessidade de verificar o resto dos campos

# O programa toma decisões fora do loop baseando-se no estado salvo
if formulario_valido:
    print("Enviando dados para o banco de dados...")
else:
    print("Erro: Por favor, preencha todos os campos obrigatórios.")
