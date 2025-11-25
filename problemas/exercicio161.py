import sqlite3

conexao = sqlite3.connect("./databases/cliente.db")
cursor = conexao.cursor()

cursor.executemany(
    """
        INSERT INTO cliente(nome, sobrenome, idade, peso, sexo, renda)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    [
        ("João", "Justino", 22, 67.9, 'M', 10000),
        ("Maria", "Cristina", 18, 65.8, 'F', 4000),
        ("Caio", "Pinto", 20, 72.8, 'M', 3500)
    ]
)

conexao.commit()
cursor.close()
conexao.close()
