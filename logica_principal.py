from orm_sqlite3 import OremPython

orm = OremPython('dbsql.db')

# orm.create_table('filme', [
#     ('id', 'INTEGER PRIMARY KEY'),
#     ('nome', 'TEXT'),
#     ('ano', 'INTEGER')
# ])

# print(orm.select_table('*', 'filme'))

# print(orm.describe_table('filme'))

# orm.insert_table('filme', (1, 'Vingadores', 2019))  # Vai inserir em (nome, ano), id é automático
# print(orm.select_table('*', 'filme'))

# orm.update_table(
#     name_of_table='filme',
#     columns_values={'ano': 2020},
#     id_primary='id',
#     id_value=1
# )

# Buscar por ID
# print(orm.get_by_id('filme', 'id', 1))

# Deletar por ID
# orm.delete_from_table('filme', 'id', 1)