import sys
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

from bbdd.bbdd import RegistroMovimientos


def obtener_ruta_trabajo():
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    return Path(__file__).parent


BASE_PATH = obtener_ruta_trabajo()
IMG_PIE = BASE_PATH / "pie_gastos.png"
IMG_BAR = BASE_PATH / "bar.png"
HTML_FILE = BASE_PATH / "informe.html"

class GeneradorInformes():
    def __init__(self, periodo):
        self.periodo = periodo

    def selector_query(self, tipo):
        match self.periodo:
            case "Últimos 30 días":
                fecha = "AND date >= date('now', '-30 days')"
            case "Últimos 6 meses":
                fecha = "AND date >= date('now', '-6 months')"
            case "Último año":
                fecha = "AND date >= date('now', '-1 year')"
            case "Todos los tiempos":
                fecha = ""

        if tipo == "gasto":
            query = f""" SELECT category as Categoría, ABS(value) as Importe
                    FROM movimientos 
                    WHERE type='{tipo}' {fecha}       
                    """
        else:
            tipo = "IN ('ingreso','gasto')"
            query = f""" SELECT type as Tipo, ABS(value) as Importe
                    FROM movimientos 
                    WHERE type {tipo} {fecha}       
                    """

        return query

    def cargar_datos(self, tipo):
        basedatos = RegistroMovimientos()
        conexion = basedatos.conectar_db()
        query = self.selector_query(tipo)
        df = pd.read_sql_query(query, con=conexion)
        conexion.close()
        return df

    def generar_graficos(self):
        #Borro archivos existentes para no mostrar datos obsoletos si por error la base de datos está vacía:
        if IMG_PIE.exists():
            IMG_PIE.unlink()
        if IMG_BAR.exists():
            IMG_BAR.unlink()

        df_gasto = self.cargar_datos("gasto")
        df_compar = self.cargar_datos("comparativa")

        if not df_compar.empty:
            #Gráfico de barras, una muestra la cantidad ingresada y la otra la gastada en el período de tiempo
            plt.figure(figsize=(15, 15))
            df_compar.groupby("Tipo")["Importe"].sum().plot(kind="bar", color=['red', 'green'])
            plt.xticks(rotation=0, fontsize=30)
            plt.yticks(fontsize=30)
            plt.ylabel("Euros(€)", fontsize=25)
            plt.tight_layout()
            plt.savefig(IMG_BAR)
            plt.close()

        if not df_gasto.empty:
            #PIE CHART con la distribucion de los gastos en funcion de la categoría
            plt.figure(figsize=(15, 15))
            df_gasto.groupby("Categoría")["Importe"].sum().plot(kind="pie", autopct='%1.1f%%', textprops={'fontsize': 30})
            plt.ylabel("")
            plt.tight_layout()
            plt.savefig(IMG_PIE)
            plt.close()

    def generar_html(self):
        self.generar_graficos()
        if IMG_PIE.exists():
            pie_html = f"<img src={IMG_PIE.name}></img>"
        else:
            pie_html = f"<p style= 'color: grey'>No hay datos de gastos para este período</p>"

        if IMG_BAR.exists():
            bar_html = f"<img src={IMG_BAR.name}></img>"
        else:
            bar_html = f"<p style= 'color: grey'>No hay datos de gastos ni ingresos para este período</p>"


        html = f"""
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Informe de ventas</title>
            <style>
                body {{ font-family: Arial; margin: 20px; }}
                img {{ width: 100%; display:block; height:auto; }}
                .contenedor{{display:flex;justify-content:space-around;}}
                .item{{text-align:center;width:45%;}}
            </style>
        </head>
        <body>
            <div class= "contenedor">
                <div class="item">
                    <h3>Distribución de gastos - {self.periodo}</h3>
                    {pie_html}
                </div>
                <div class="item">
                    <h3>Balance total (€) - {self.periodo}</h3>
                    {bar_html}
                </div>
            </div>
        </body>
        </html>
        """
        HTML_FILE.write_text(html,encoding="utf-8")

