import os

import oracledb
from dotenv import load_dotenv

load_dotenv()


def conect_database():
    host = os.getenv("ORACLE_HOST")
    port = os.getenv("ORACLE_PORT")
    service_name = os.getenv("ORACLE_SERVICE_NAME")
    user = os.getenv("ORACLE_USER")
    password = os.getenv("ORACLE_PASSWORD")

    dsn = f"{host}:{port}/{service_name}"

    conn = oracledb.connect(
        user=user,
        password=password,
        dsn=dsn,
    )
    print("Conectado com sucesso!")

    return conn


def close_database(conn):
    try:
        conn.close()
        print("Fechado com sucesso!")
        return True
    except Exception:
        print("Banco não fechado!")


def create(conn, tipo_pet, nome_pet, idade):
    tipo_pet = tipo_pet.lower()
    nome_pet = nome_pet.lower()
    with conn.cursor() as cursor:
        cursor.execute("""
        INSERT INTO petshop (tipo_pet, nome_pet, idade)
        VALUES (:1, :2, :3)
    """, [tipo_pet, nome_pet, idade])
    conn.commit()
    tipo_pet = tipo_pet.title()
    nome_pet = nome_pet.title()
    print(f"Pet Cadastrado - {tipo_pet}({nome_pet=}, {idade=})")


def read(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, tipo_pet, nome_pet, idade FROM petshop")

        rows = cursor.fetchall()

        if not rows:
            print("Nenhum registro encontrado.")
            return []

        print("Listando...")
        for row in rows:
            print(row)

        return rows


def read_one(conn, id):
    with conn.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, tipo_pet, nome_pet, idade
            FROM petshop WHERE id=:1
            """, [id]
        )
        row = cursor.fetchone()

        if row:
            print("Retornando...")
            print(row)
            return row
        else:
            print("Nenhum registro encontrado.")
            return None


def update(conn, id, novo_tipo, novo_nome, nova_idade):
    novo_tipo = novo_tipo.lower()
    novo_nome = novo_nome.lower()
    anterior = read_one(conn, id)
    if not anterior:
        return
    _, tipo, nome, idade = anterior
    with conn.cursor() as cursor:
        cursor.execute(
            """
            UPDATE petshop
            SET tipo_pet=:2, nome_pet=:3, idade=:4
            WHERE id=:1
            """, [id, novo_tipo, novo_nome, nova_idade]
        )
        conn.commit()
        print("PET ALTERADO COM SUCESSO!")
        tipo = tipo.title()
        nome = nome.title()
        novo_tipo = novo_tipo.title()
        novo_nome = novo_nome.title()
        print(f"ANTERIOR - {tipo}({nome=}, {idade=})")
        print(f"ATUAL - {novo_tipo}({novo_nome=}, {nova_idade=})")


def delete(conn, id):
    anterior = read_one(conn, id)

    if not anterior:
        print("Registro não encontrado.")
        return

    with conn.cursor() as cursor:
        cursor.execute(
            "DELETE FROM petshop WHERE id = :1",
            [id]
        )
        conn.commit()

    _, tipo, nome, idade = anterior
    tipo = tipo.title()
    nome = nome.title()

    print(f"Deletado: {tipo}(nome={nome}, idade={idade})")


def delete_all(conn):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM petshop")
        conn.commit()

    print("Todos os registros foram deletados.")


if __name__ == "__main__":
    conn = conect_database()
    # create(conn, "Cachorro", "Batata", 3)
    # read(conn)
    # read_one(conn, 1)
    # update(conn, 2, "Cachorro", "Batata", 5)
    # delete(conn, 2)
    close_database(conn)
