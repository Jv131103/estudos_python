import sqlite3
from contextlib import closing

with sqlite3.connect('./databases/dados_alunos.db') as conn:
    with closing(conn.cursor()) as cursor:

        # cria a tabela alunos
        sql = """
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(55) NOT NULL,
            idade INTEGER NOT NULL,
            telefone VARCHAR(15) NOT NULL,
            profissao VARCHAR(30) NOT NULL
        )
        """
        cursor.execute(sql)

        # inserindo registros
        dados = [
            ('Yun', 29, '+00000000', 'Músico'),
            ('Chan', 37, '+00000000', 'Engenheiro Elétrico'),
            ('Ayumi', 41, '+00000000', 'Programador'),
            ('Hinata', 25, '+00000000', 'Professor')
        ]

        sql = """INSERT INTO alunos(nome,idade,telefone,profissao) VALUES(?,?,?,?)"""
        cursor.executemany(sql, dados)

        # Mostra os dados
        resultados = cursor.execute("SELECT * FROM alunos")
        for registro in resultados:
            print(f'id: {registro[0]}')
            print(f'Nome: {registro[1]}')
            print(f'Idade: {registro[2]}')
            print(f'Telefone: {registro[3]}')
            print(f'Profissão: {registro[4]}')
            print()
