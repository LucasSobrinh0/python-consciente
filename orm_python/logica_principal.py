from orm_sqlite3 import OremPython

# Inicializa o ORM com o banco de dados
orm = OrmPython('dbsql.db')

# 1. Criar a tabela 'filme'
orm.create_table('filme', [
    ('id', 'INTEGER PRIMARY KEY'),
    ('nome', 'TEXT'),
    ('ano', 'INTEGER')
])

# 2. Inserir dados na tabela
orm.insert_table('filme', (1, 'Vingadores: Ultimato', 2019))
orm.insert_table('filme', (2, 'Kung Fu Panda 4', 2024))
orm.insert_table('filme', (3, 'Um filme minecraft', 2025))

# 3. Selecionar todos os dados
print("== Todos os filmes ==")
print(orm.select_table('*', 'filme'))

# 4. Selecionar somente o nome dos filmes
print("== Nome dos filmes ==")
print(orm.select_table(['nome'], 'filme'))

# 5. Descrever a tabela (estrutura)
print("== Estrutura da tabela ==")
print(orm.describe_table('filme'))

# 6. Atualizar o ano de um filme
orm.update_table('filme', {'ano': 2020}, 'id', 1)

# 7. Buscar um filme pelo ID
print("== Filme com ID = 1 ==")
print(orm.get_by_id('filme', 'id', 1))

# 8. Deletar um filme
orm.delete_from_table('filme', 'id', 2)

# 9. Verificar dados finais
print("== Filmes após deleção ==")
print(orm.select_table('*', 'filme'))
