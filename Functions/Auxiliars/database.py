import sqlite3 as sql
import sys

DATABASE_PATH = 'sme.db'

if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'Tests/smetest.db'

class ConnectionCommit:
    def __init__(self, db_file):
        self.connection = sql.connect(db_file)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An exception of type {exc_type.__name__} occurred with value {exc_value}")
            if traceback is not None:
                print("Traceback:")

        self.connection.commit()
        self.connection.close()

class SimpleConnection:
    def __init__(self, db_file):
        self.connection = sql.connect(db_file)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An exception of type {exc_type.__name__} occurred with value {exc_value}")
            if traceback is not None:
                print("Traceback:")
                traceback.print_tb(traceback)

        self.connection.close()

class DatabaseFunctions:
    @staticmethod
    def create_tables(case):
        with SimpleConnection(DATABASE_PATH) as cursor:
            match case:
                case '1':
                    cursor.execute('CREATE TABLE IF NOT EXISTS clients'\
                                '(id VARCHAR PRIMARY KEY, name VARCHAR, surname VARCHAR, gender VARCHAR, age INTEGER)')
                case '2':
                    cursor.execute('CREATE TABLE IF NOT EXISTS sales'\
                                '(id VARCHAR PRIMARY KEY, client_id VARCHAR, date VARCHAR, cash INTEGER, transaction_state VARCHAR, service_state VARCHAR, FOREIGN KEY (client_id) REFERENCES clients(id))')
                case '3':    
                    cursor.execute('CREATE TABLE IF NOT EXISTS workers'\
                                '(id VARCHAR PRIMARY KEY, name VARCHAR, surname VARCHAR, position VARCHAR, salary INTEGER)')

    @staticmethod        
    def load_from_table(model_table, model_class):
        with SimpleConnection(DATABASE_PATH) as cursor:
            content = cursor.execute(f'SELECT * FROM {model_table}').fetchall()
            registers = [model_class(*param) for param in content]
            return registers

    @staticmethod    
    def insert_register(model_table, model_colums, register_columns):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            place_columns = ', '.join(model_colums)
            place_holders = ', '.join(['?' for _ in register_columns])
            try:
                cursor.execute(f'INSERT INTO {model_table}({place_columns}) VALUES({place_holders})', register_columns)
            except sql.IntegrityError:
                print(f'The {model_table} exits')

    @staticmethod
    def update_register(model_table, model_colums, register_columns):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            place_columns = ', '.join(f'{column} = ?' for column in model_colums)
            cursor.execute(f'UPDATE {model_table} SET {place_columns} WHERE id = ?', register_columns)

    @staticmethod
    def delete_register(model_table, condition):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            cursor.execute(f'DELETE FROM {model_table} WHERE id = ?', (condition,))

    @staticmethod
    def remove_all_registers(model_table):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            cursor.execute(f'DELETE FROM {model_table};')