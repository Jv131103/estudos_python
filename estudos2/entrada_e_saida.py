# Entrada
nome = input("Digite o seu nome: ")

# Saída
print(f"Olá {nome}")

# O input(), por padrão interpreta tudo como string
# Então se não quero que isso ocorra em certos momentos posso chamar

# int() -> Se quero números inteiros. Só números, e nada além
idade = int(input("Digite a sua idade: "))
print(f"Sua idade é {idade} anos")

# float() -> Se quero números decimais. Só numeros
# O . é fundamental e aceito e utilize apenas ele como diferencial
# Caso usar a , por exemplo, gerará erro
peso = float(input("Digite o seu peso: "))
print(f"Seu peso é {peso}")
# Você pode formatar a saída de casas decimais
print(f"Repito: Seu peso é {peso:.2f}")  # :.2f diz: Duas casas decimais

# str() -> Para string, embora o input, já faça isso
sobrenome = str(input("Seu sobrenome: "))
print(f"{sobrenome} é um sobrenome bonito!")

# complex() -> Mais avançado, usado em matemática para representar complexos
# Sua leitura, pode conter números e letras e pode ser representado com +
# EX de leitura válida: 123+1j (Só j pode se considerar e no final da chamada)
print(f"{idade} em complexo é igual a {complex(idade)}")  # Isso pode ser feito para as anteriores também, bem como funções, procedimentos, etc.
