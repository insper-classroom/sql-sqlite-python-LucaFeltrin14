from db import db_utils



db_utils.criar_tabela("Estudantes")

estudantes = [
    ('Ana Silva' , 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]

db_utils.inserir_estudante("Estudantes", estudantes)

db_utils.atualiza_registro("Estudantes", 2021, "João Alves")

db_utils.deleta_registro("Estudantes", 1)

db_utils.update_ano_curso("Estudantes", 2018, "Computação")

db_utils.select_estudantes("Estudantes", "Computação", 2019)

db_utils.select_ano("Estudantes", 2019)

db_utils.mostra_registros("Estudantes")

db_utils.close()