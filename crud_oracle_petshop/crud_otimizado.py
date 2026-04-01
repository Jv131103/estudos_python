import os

import oracledb
from dotenv import load_dotenv

load_dotenv()


def connect_database():
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
    except Exception as e:
        print(f"Banco não fechado: {e}")
        return False


def create(conn, tipo_pet, nome_pet, idade):
    try:
        tipo_pet = tipo_pet.strip().lower()
        nome_pet = nome_pet.strip().title()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO petshop (tipo_pet, nome_pet, idade)
                VALUES (:1, :2, :3)
                """,
                [tipo_pet, nome_pet, idade]
            )
        conn.commit()
        print(f"Pet cadastrado - {tipo_pet.title()} (nome={nome_pet}, idade={idade})")
    except Exception as e:
        print(f"Erro ao cadastrar pet: {e}")


def read(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, tipo_pet, nome_pet, idade FROM petshop")
        return cursor.fetchall()


def read_one(conn, pet_id):
    with conn.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, tipo_pet, nome_pet, idade
            FROM petshop
            WHERE id = :1
            """,
            [pet_id]
        )
        return cursor.fetchone()


def update(conn, pet_id, novo_tipo, novo_nome, nova_idade):
    anterior = read_one(conn, pet_id)

    if not anterior:
        print("Registro não encontrado.")
        return

    try:
        novo_tipo = novo_tipo.strip().lower()
        novo_nome = novo_nome.strip().title()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE petshop
                SET tipo_pet = :2,
                    nome_pet = :3,
                    idade = :4
                WHERE id = :1
                """,
                [pet_id, novo_tipo, novo_nome, nova_idade]
            )
        conn.commit()

        _, tipo_ant, nome_ant, idade_ant = anterior

        print("Pet alterado com sucesso!")
        print(f"ANTERIOR - {tipo_ant.title()} (nome={nome_ant.title()}, idade={idade_ant})")
        print(f"ATUAL - {novo_tipo.title()} (nome={novo_nome}, idade={nova_idade})")

    except Exception as e:
        print(f"Erro ao atualizar pet: {e}")


def delete(conn, pet_id):
    anterior = read_one(conn, pet_id)

    if not anterior:
        print("Registro não encontrado.")
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM petshop WHERE id = :1", [pet_id])
        conn.commit()

        _, tipo, nome, idade = anterior
        print(f"Deletado: {tipo.title()} (nome={nome.title()}, idade={idade})")

    except Exception as e:
        print(f"Erro ao deletar pet: {e}")


def delete_all(conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE petshop")
        print("Todos os registros foram deletados.")
    except Exception as e:
        print(f"Erro ao deletar todos os registros: {e}")
