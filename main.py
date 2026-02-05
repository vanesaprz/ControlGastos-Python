import sys
from pathlib import Path

from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QHeaderView, QTableWidgetItem
from ui.ventana_1 import Ui_MainWindow
from PySide6.QtCore import QUrl

from bbdd.bbdd import RegistroMovimientos
from dialogo_movimiento import DialogoMovimiento
from generar_informes import GeneradorInformes
from PySide6.QtWebEngineWidgets import QWebEngineView

HTML_FILE = Path("informe.html")

class ControlGastos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AppAhorro")
        self.baseDatos = RegistroMovimientos()
        # Interfaz principal:
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # BOTONES PRINCIPALES
        self.ui.b_tablero.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.b_informes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.b_informes.clicked.connect(self.generar_informes)
        self.ui.btn_gasto.clicked.connect(lambda: self.ventana_movimiento("gasto"))
        self.ui.btn_ingreso.clicked.connect(lambda: self.ventana_movimiento("ingreso"))
        self.ui.eliminar_seleccion.clicked.connect(self.eliminar_movimiento_seleccionado)
        #INDICAMOS EL BALANCE:
        self.guardar_balance()


        #BOTON INFORMES:
        self.ui.btn_gen_informes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btn_gen_informes.clicked.connect(self.generar_informes)


       #Modificamos la tabla de movimiento, adaptamos los anchos y ocultamos la columna ID
        self.ui.movimientos_tabla.setColumnHidden(0, True)
        self.ui.movimientos_tabla.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        self.web = QWebEngineView()
        self.ui.html_layout.addWidget(self.web)

        #Rellenamos la tabla con los movimientos históricos:
        self.rellenar_tabla("SELECT * FROM movimientos ORDER BY date DESC")

        #MENU
        self.ui.action_NuevoGasto.triggered.connect(lambda: self.ventana_movimiento("gasto"))
        self.ui.action_NuevoIngreso.triggered.connect(lambda: self.ventana_movimiento("ingreso"))
        self.ui.actionVerInformes.triggered.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.actionTablero_Principal.triggered.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

        #modifico el estilo de la aplicación
        self.setStyleSheet("""
            QMainWindow {
                background-color: #EBF4F6;
            }

            QPushButton {
                background-color: #09637E;
                color: white;
                border-radius: 8px;
                padding:10px 20px;
                font-weight: bold;
                border: solid;
                margin-bottom: 5px;
            }

            QPushButton:hover {
                background-color: #088395;
                
            }

            QPushButton#eliminar_seleccion {
                background-color: #FFA4A4;
            }
            QPushButton#eliminar_seleccion:hover {
                background-color: #FFBDBD;
            }

            QTableWidget {
                background-color: white;
                border-radius: 10px;
                gridline-color: #e2e8f0;
                alternate-background-color: #f8fafc;
                selection-background-color: #dbeafe;
                selection-color: #1e40af;
            }

            QHeaderView::section {
                background-color: #f1f5f9;
                padding: 6px;
                border: none;
                font-weight: bold;
                color: #64748b;
            }

        """)


    def ventana_movimiento(self, tipo):
        # Creamos el diálogo personalizado
        dialogo = DialogoMovimiento(tipo)
        if dialogo.exec() == QDialog.Accepted:
            datos = dialogo.obtener_datos()
            try:
                self.baseDatos.introducir_movimiento(
                    datos["fecha"], datos["tipo"], datos["categoria"],
                    datos["descripcion"], datos["valor"]
                )
                print("Guardado con éxito")
                # Actualizamos la interfaz principal
                self.rellenar_tabla("SELECT * FROM movimientos ORDER BY date DESC")
                self.guardar_balance()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Error al guardar: {e}")


    #dejo la query fuera porque da posibilidades de calcular otros periodos de tiempo en otro momentos si se quisiera
    def rellenar_tabla(self, query):

        movimientos = self.baseDatos.devolver_movimientos(query)
        self.ui.movimientos_tabla.setRowCount(len(movimientos))

        for fila in range(0, len(movimientos)):
            for columna in range(6):
                dato=str(movimientos[fila][columna])
                item = QTableWidgetItem(dato)
                self.ui.movimientos_tabla.setItem(fila, columna, item)


    def guardar_balance(self):
        try:
            balance = self.baseDatos.devolver_balance_total()
            self.ui.resumen_dinero.setText(f"{balance:.2f}")
            if balance > 0:
                self.ui.resumen_dinero.setStyleSheet("color:#5D866C")
            if balance < 0:
                self.ui.resumen_dinero.setStyleSheet("color:#FFA4A4")
        except Exception as e:
            self.ui.resumen_dinero.setText(f"0.00")


    def eliminar_movimiento_seleccionado(self):
        resultado = self.ui.movimientos_tabla.selectedItems()
        if not resultado:
            QMessageBox.warning(self,"Aviso", "No hay movimiento seleccionado")
            return

        fila = self.ui.movimientos_tabla.row(resultado[0])
        item_id = self.ui.movimientos_tabla.item(fila,0)

        if item_id:
            id_movimiento =int(item_id.text())
            self.baseDatos.eliminar_movimiento(id_movimiento)

        self.rellenar_tabla("SELECT * FROM movimientos ORDER BY date DESC")
        self.guardar_balance()

    def generar_informes(self):
        periodo = self.ui.combo_informes.currentText()
        generador = GeneradorInformes(periodo)
        try:
            generador.generar_html()
            self.web.setUrl(QUrl.fromLocalFile(str(HTML_FILE.resolve())))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication()
    ventana = ControlGastos()
    ventana.show()
    sys.exit(app.exec())
