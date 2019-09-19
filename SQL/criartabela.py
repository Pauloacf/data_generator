import sqlite3


def create_table():
    conn = sqlite3.connect('./SQL/tabela.sql')
    cursor = conn.cursor()

    # criando tabela
    cursor.execute("""
    CREATE TABLE tabela (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        telefone TEXT,
        rua TEXT,
        uf TEXT,
        cep TEXT
    );
    """)

    print('tabela criada')
