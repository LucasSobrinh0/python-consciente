import sqlite3 # Importa o sqlite3

class OremPython:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def create_table(self, name_of_table, columns: list):
        """
        CREATE TABLE IF NOT EXISTS filme[('id', 'INTEGER PRIMARY KEY'),
        ('nome', 'TEXT'),
        ('ano', 'INTEGER')]
        """
        try:
            column_defs = ", ".join([f"{col} {type_}" for col, type_ in columns]) # list comprehension
            self.cur.execute(f"CREATE TABLE IF NOT EXISTS {name_of_table}({column_defs})")
            self.con.commit()
        except sqlite3.Error as e:
            print("Erro ao criar tabela:", e)


    def select_table(self, columns, name_of_table):
        """
            SELECT 'nome' FROM 'filme';
            SELECT * from 'filme'
        """

        try:
            if columns == '*':
                cols = '*'
            else:
                cols = ", ".join(columns)
            result = self.cur.execute(f"SELECT {cols} FROM {name_of_table}")
            return result.fetchall()
        except sqlite3.Error as e:
            print("Erro ao selecionar:", e)
            return []
    
    def describe_table(self, name_of_table):
        """
        PRAGMA table_info ('filme')
        """
        try:
            result = self.cur.execute(f"PRAGMA table_info ({name_of_table})")
            return result.fetchall()
        except sqlite3.Error as e:
            print("Erro ao descrever tabela:", e)

    def insert_table(self, name_of_table, values_columns):
        """
        INSERT INTO 'filme' VALUES (2, 'Kong Fu Panda 4', 2024)
        """
        try:
            placeholders = ", ".join(["?"] * len(values_columns))
            self.cur.execute(f"INSERT INTO {name_of_table} VALUES ({placeholders})", values_columns) #list comprehension
            self.con.commit()
        except sqlite3.Error as e:
            print("Houve um erro ao inserir os dados na tabela.", e)
    
    def update_table(self, name_of_table, columns_values: dict, id_primary, id_value):
        """
        UPDATE 'filme' SET 'ano': 2020 WHERE 'id' = 1;
        """
        try:
            set_clause = ", ".join([f"{col} = ?" for col in columns_values.keys()]) # list comprehension
            values = list(columns_values.values()) + [id_value]

            self.cur.execute(
                f"UPDATE {name_of_table} SET {set_clause} WHERE {id_primary} = ?",
                values
            )
            self.con.commit()
        except sqlite3.Error as e:
            print("Houve um erro ao atualizar os dados na tabela.", e)
    
    def delete_from_table(self, name_of_table, id_primary, id_value):
        """
        DELETE FROM 'filme' WHERE 'id' = 2
        """
        try:
            self.cur.execute(
                f"DELETE FROM {name_of_table} WHERE {id_primary} = ?",
                (id_value,)
            )
            self.con.commit()
        except sqlite3.Error as e:
            print("Houve um erro ao deletar os dados da tabela.", e)

    def get_by_id(self, name_of_table, id_primary, id_value):
        """
        SELECT * FROM 'filme' WHERE 'id' = 1;
        """
        try:
            result = self.cur.execute(
                f"SELECT * FROM {name_of_table} WHERE {id_primary} = ?",
                (id_value,)
            )
            return result.fetchone()
        except sqlite3.Error as e:
            print("Houve um erro ao buscar o registro.", e)
            return None
