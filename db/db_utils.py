import sqlite3

conn = sqlite3.connect('db/database_alunos2.db')
cursor = conn.cursor()

def criar_tabela(nome_tab):
    cursor.execute(f"DROP TABLE IF EXISTS {nome_tab}")
    conn.commit()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {nome_tab} (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoDeIngresso INTEGER
);
""")
    conn.commit()

def inserir_estudante(nome_tab , estudantes):
    cursor.executemany(f"""
    INSERT INTO {nome_tab} (Nome, Curso, AnoDeIngresso)
    VALUES (?, ?, ?);
    """, estudantes)
    conn.commit()

def mostra_registros(nome_tab):
    cursor.execute(f"SELECT * FROM {nome_tab}")
    print(cursor.fetchall())

def atualiza_registro(nome_tab, ano, nome):
    cursor.execute(f"UPDATE {nome_tab} SET AnoDeIngresso = ? WHERE Nome = ?", (ano, nome))
    conn.commit()

def deleta_registro(nome_tab, id): 
    cursor.execute(f"DELETE FROM {nome_tab} WHERE ID = ?", (id,))
    conn.commit()

def update_ano_curso(nome_tab, ano, curso):
    cursor.execute(f"UPDATE {nome_tab} SET AnoDeIngresso = ? WHERE Curso = ?", (ano, curso))
    conn.commit()

def select_estudantes(nome_tab, curso, ano):
    cursor.execute(f"SELECT * FROM {nome_tab} WHERE Curso = ? AND AnoDeIngresso > ?", (curso, ano))
    print(cursor.fetchall())

def select_ano(nome_tab, ano):
    cursor.execute(f"SELECT * FROM {nome_tab} WHERE AnoDeIngresso BETWEEN ? AND ?", (ano, ano+1))
    print(cursor.fetchall())

def close():
    conn.close()