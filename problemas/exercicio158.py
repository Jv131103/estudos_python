import sqlite3

conexao = sqlite3.connect("./databases/estoque.db")
cursor = conexao.cursor()

# deleta a tabela CLIENTE caso já exista
cursor.execute('DROP TABLE IF EXISTS estoque')

cursor.execute(
    '''
        CREATE TABLE estoque(
            nome TEXT,
            preco FLOAT,
            quantidade INT
        )
    '''
)

conexao.commit()
cursor.close()
conexao.close()
