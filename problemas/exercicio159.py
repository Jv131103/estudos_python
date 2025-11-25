import sqlite3

conexao = sqlite3.connect("./databases/cliente.db")
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sobrenome TEXT,
            idade INTEGER,
            peso REAL,
            sexo TEXT,
            renda REAL
        );
    '''
)

conexao.commit()
cursor.close()
conexao.close()
