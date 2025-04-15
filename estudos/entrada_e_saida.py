mensagem = input("Minha mensagem: ")  # Entrada recebida
print(mensagem)  # Saída retornada

# Referenciando os tipos primitivos...
# Por padrão, todo input, será um valor do tipo string, logo...
idade = input("Digite a sua idade: ")
print("Sua idade é:", idade)
print("Tipo de dado:", type(idade))  # <class 'str'>
# Logo, se precisarmos realizar um cálculo, ou verificar por tipos, isso
# se torna um problema, mas o python, nos dá a solução:

# Covertemos para inteiro
# PS, digite apenas números inteiros, e nada mais, caso contrário, teremos um erro de tipo
idade = int(input("Digite a sua idade: "))
print("Sua idade é:", idade)
print("Tipo de dado:", type(idade))  # <class 'int'>

# Converte para ponto flutuante, mas jamais faça: 3,14 e sim 3.14, isso é um padrão do inglês
# PS, digite apenas números reais ou inteiros, caso contrário, termos erro de tipo
salario = float(input("Seu salário: "))
print("Seu salário é:", salario)
print("Tipo de dado:", type(salario))  # <class 'float'>

# Também pode
nome = str(input("Seu nome: "))  # Não necessário, pois o input em si é STR()
print("Seu nome é", nome)
print("Tipo de dado:", type(nome))  # <class 'str'>

# Converte para booleano
# PS, tudo que for diferente de 0 ou ""(LÊ-SE: string vazia), retornará True
algo = bool(input("Digite algo: "))
print("É True ou False?", algo)
print("Tipo de dado:", type(algo))  # <class 'bool'>
