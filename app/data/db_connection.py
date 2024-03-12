import os
import sqlite3
from sqlite3 import Error

class DatabaseConnection:
    def __init__(self):
        self.database_name = "LyonSystem.db"
        self.database_path = "app/data/"
        self.connection = self.create_connection()

    def create_connection(self):
        db_path = os.path.join(self.database_path, self.database_name)
        
        if not os.path.exists(db_path):
            print(f"Error: La base de datos '{self.database_name}' no existe.")
            return None

        try:
            connection = sqlite3.connect(db_path)
            print("Conexión a la base de datos exitosa.")
            return connection
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def execute_query(self, query, parameters=None):
        cursor = self.connection.cursor()
        try:
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)
            print("Query ejecutada con éxito.")
        except Error as e:
            print(f"Error al ejecutar la query: {e}")

    def commit(self):
        self.connection.commit()
        print("Commit realizado con éxito.")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Conexión a la base de datos cerrada.")
