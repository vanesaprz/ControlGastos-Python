import unittest
import os
from pathlib import Path


from bbdd.bbdd import RegistroMovimientos
from datetime import date


class TestControlGastos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #base de datos de prueba para no borrar datos reales.
        cls.db_nombre = "test_datos.db"
        cls.repositorio = RegistroMovimientos(cls.db_nombre)

    def setUp(self):
    # Limpiamos la tabla para que cada test empiece de cero
        with self.repositorio.conectar_db() as conexion:
            conexion.execute("DELETE FROM movimientos")

    def test_movimiento_calculo (self):
        #Introducimos un ingreso y un gasto:
        self.repositorio.introducir_movimiento(date(2026, 2, 5), "ingreso", "Nómina", "Sueldo", 1500)
        self.repositorio.introducir_movimiento(date(2026, 2, 5), "gasto", "Vivienda", "Alquiler", -600)

        #Verificamos que el balance obtenido es correcto:
        balance = self.repositorio.devolver_balance_total()
        self.assertEqual(balance, 900)

    def test_eliminar_movimientos (self):
        self.repositorio.introducir_movimiento(date(2026, 2, 5), "ingreso", "Nómina", "Borrar", 2000)
        movimientos = self.repositorio.devolver_movimientos("SELECT id FROM movimientos WHERE description='Borrar'")
        id_borrar = movimientos[0][0]

        self.repositorio.eliminar_movimiento(id_borrar)
        comprobacion = self.repositorio.devolver_movimientos(f"SELECT id FROM movimientos WHERE id = {id_borrar}")

        self.assertEqual(len(comprobacion), 0)


    @classmethod
    def tearDownClass(cls):
        #sin esto no me eliminaba el archivo:
        del cls.repositorio

        #indicamos la ubicacion de la base de datos del test para poder eliminarlo
        ruta_proyecto = Path(__file__).resolve().parent
        db_path = ruta_proyecto / "bbdd" / cls.db_nombre

        if db_path.exists():
            try:
                os.remove(db_path)
                print(f"Archivo {cls.db_nombre} eliminado con éxito.")
            except Exception as e:
                print(f"Error al eliminar: {e}")

if __name__ == "__main__":
    unittest.main()