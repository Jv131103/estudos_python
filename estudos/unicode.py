limite = 128  # Defina seu limite aqui

# Tabela Unicode (primeiros 128 caracteres são a mesma que a ASCII)
print("Tabela Unicode:")
for i in range(limite):
    print(f"U+{i:04X}: {chr(i)}")
