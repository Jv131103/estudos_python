import sqlite3

conexao = sqlite3.connect("./databases/estoque.db")
cursor = conexao.cursor()

cursor.executemany(
    """
        INSERT INTO estoque(nome, preco, quantidade)
        VALUES (?, ?, ?)
    """,
    [
        ("Processador Intel Core I5 12° geração", 4300.3, 6),
        ("Memória RAM Kingston 32 gb M4", 225.75, 10)
    ]
)

conexao.commit()
cursor.close()
conexao.close()
