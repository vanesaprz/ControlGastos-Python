import sqlite3 as sql
from datetime import datetime, date
from pathlib import Path
import sys

#----
#Haciendo el test me dio error en el "default date adapter" esta es una de las soluciones que encontré
sql.register_adapter(date, lambda d: d.isoformat())
sql.register_adapter(datetime, lambda dt: dt.isoformat())
#-----
class RegistroMovimientos:
    def __init__(self, db_name="datos.db"):
        if getattr(sys, 'frozen', False):
            self.ruta_base = Path(sys.executable).parent
        else:
            self.ruta_base=Path(__file__).resolve().parent
        self.db_path= self.ruta_base / db_name
        self.inicializar_db()

    def conectar_db(self):
        conexion = sql.connect(self.db_path)
        return conexion

    def inicializar_db(self):
        # se crean las tablas de movimientos y el perfil si no existen ya
        with self.conectar_db() as conexion:
            sql_tabla_movimientos = """
            CREATE TABLE IF NOT EXISTS movimientos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,            
            description VARCHAR(255) NOT NULL,
            category VARCHAR NOT NULL,            
            value double NOT NULL,
            type VARCHAR(7) NOT NULL)            
            """

            conexion.execute(sql_tabla_movimientos)


    def introducir_movimiento(self, date, type, category, description, value):
        query = (f"INSERT INTO movimientos (date, type, category, description, value)"
                 f"VALUES (?, ?, ?, ?, ?) ")

        with self.conectar_db() as conexion:
            conexion.execute(query, (date, type, category, description, value))

    def devolver_movimientos(self, query):
        with self.conectar_db() as conexion:
            cursor = conexion.cursor()
            resultado = None
            try:
                cursor.execute(query)
                resultado = cursor.fetchall()

            except Exception as e:
                print(f"El error {e} ha ocurrido")
            return resultado

    def devolver_balance_total(self):
        with self.conectar_db() as conexion:
            balance = conexion.execute("SELECT SUM(value) FROM movimientos")
            return balance.fetchone()[0]

    def eliminar_movimiento(self, clave):
        query = (f"DELETE FROM movimientos WHERE id = ?")
        with self.conectar_db() as conexion:
            conexion.execute(query, (clave,))