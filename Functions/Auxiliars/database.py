import sqlite3 as sql
import sys

DATABASE_PATH = 'sme.db'

if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'Tests/sme_test.db'

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
                traceback.print_tb(traceback)

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