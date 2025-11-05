# estruturas condicionais, são blocos de código que nos permite executar
# ações de diferentes caminhos, ou seja, com eles, podemos diversificar
# como o nosso código executará em certos contextos.
# Em condicionais uma estrutura só será verdadeira se uma condição for
# verdadeira.
# Em lógica, uma condição só será falsa se uma proposição a direita for falsa
# ESTRUTURA:
# if <condição>:
#   <bloco>
# else:
#   <bloco>

# um if só será verdade se pelo menos a afirmação for verdade:
if True:
    print("Executo sempre")
if False:
    print("NUNCA SEREI EXECUTADO")

# if solitário
# Podemos definir ifs de forma solitária sem complementos, criando um bloco
# específico antes de voltar ao global
numero = 10
if numero >= 10:
    print(numero)
print("Seguindo")

# if com if. com ele, podemos definir N bloco autônomos criando blocos
# independentes um do outro de forma específica antres de voltar ao global
conectivo = "e"
if conectivo == "e":
    print("Só será verdade se ambas as proposições forem verdades")

if conectivo == "ou":
    print("Será verdadeiro se pelo menos uma proposição for verdadeira")

print("Seguindo")

# if else. Se algo for verdadeiro, ele passará pelo if, caso contrário,
# passará pelo else. Todo else precisa de if ou pelos menos de uma contra
# afirmativa, ou seja, ele é um escape que pode executar algo específico se
# nenhuma análise for verdadeira
idade = 18
if idade >= 18:
    print("ADULTO")
else:
    print("KID")
print("Seguindo")

# if elif. O elif é uma forma elegante de definir uma contraposição do if,
# se ele não for verdadeiro, e também só lerá o bloco, se ele for verdadeiro.
# Logo, se a primeira condição for falsa, vai passando pela outra e assim vai.
# Pode-se ter N elifs alinhados ao if. Um elif, obrigatoriamente, pelo menos na
# primeira definição, precisa de um if para executar.
nome = "João"
if nome == "José":
    print("DÁ PARA SER MELHOR")
elif nome == "Josias":
    print("AINDA DÁ PARA MELHORAR")
elif nome == "João":
    print("AGORA FICOU BOM")
print("Seguindo")

# if elif else. O TRIO PARADA DURA, É uma forma de definir afirmações
# e verificar item por item, tal que se o if e os elifs forem falsos,
# partirão para o else e executará um bloco específico. Essa é uma forma
# eficiente e mais elegante de se fazer verificações lógicas, porém,
# ambos dependem de um único if e um só executará o outro se pelo menos uma
# afirmativa for falsa
opcao = "abrir"
if opcao == "abrir":
    print("Abrindo...")
elif opcao == "reiniciar":
    print("reiniciando")
elif opcao == "converter":
    print("Convertendo")
else:
    print("FALLBACK, MANTENDO A APLICAÇÃO")

# ifs aninhados. Podemos aninhar condicionais, criando outras condicionais.
# Mas cuidado com o haduken identation, ou seja, criando muitos ifs de forma
# desnecessária. Muitas condicionais, podem tornar o código ilegível e lento.
idade = 20
tem_carteira = True

# se quisesse, poderia só ter um if solitário também
if idade >= 18:
    print("É maior de idade.")
    if tem_carteira:
        print("Pode dirigir.")
    else:
        print("Maior de idade, mas não tem carteira.")
else:
    print("Menor de idade, não pode dirigir.")

# Exemplo de if / elif aninhado
nota = 8
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
    if nota >= 8.5:
        print("Mas ainda pode melhorar para excelente!")
    elif nota >= 8.9:
        print("faltou pouco para 9")
    else:
        print("Continue estudando para subir mais!")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# HADOUKEN INDENTATION (exemplo ruim)
usuario_logado = True
permissao_admin = True
sistema_online = True
dados_carregados = True

if usuario_logado:
    if permissao_admin:
        if sistema_online:
            if dados_carregados:
                print("Tudo certo, acesso liberado!")
            else:
                print("Erro: dados não carregados")
        else:
            print("Erro: sistema offline")
    else:
        print("Sem permissão de admin")
else:
    print("Usuário não logado")
