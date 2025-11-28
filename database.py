# database.py
import sqlite3
from pathlib import Path

DB_PATH = Path("carteiras_de_habilitacao.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # permite acessar colunas por nome
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS carteiras_habilitacao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            sobrenome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            nacionalidade TEXT NOT NULL,
            categoria TEXT NOT NULL,
            data_emissao TEXT NOT NULL,
            validade TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

def deletar_tabela_temporariamente():
    conn = get_connection()
    cur = conn.cursor()
    # Comando SQL para deletar a tabela
    cur.execute("DROP TABLE IF EXISTS carteiras_habilitacao")
    conn.commit()
    conn.close()