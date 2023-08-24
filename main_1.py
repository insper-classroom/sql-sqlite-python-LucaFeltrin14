import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoDeIngresso INTEGER
);
""")

estudantes = [
    ('Ana Silva' , 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]

# cursor.executemany("""
# INSERT INTO Estudantes (Nome, Curso, AnoDeIngresso)
# VALUES (?, ?, ?);
# """, estudantes)

# conn.commit()
cursor.execute("SELECT * FROM Estudantes WHERE AnoDeIngresso = 2019 OR AnoDeIngresso = 2020")

cursor.execute("UPDATE Estudantes SET AnoDeIngresso = ? WHERE Nome = ?", (2021, "João Alves"))

cursor.execute("DELETE FROM Estudantes WHERE ID = ?", (1,))

cursor.execute("SELECT * FROM Estudantes WHERE Curso = 'Computação' AND AnoDeIngresso > 2019")

cursor.execute("UPDATE Estudantes SET AnoDeIngresso = ? WHERE Curso = ?", (2018, "Computação"))

cursor.execute("SELECT * FROM Estudantes")

print(cursor.fetchall())
conn.commit()

conn.close()
