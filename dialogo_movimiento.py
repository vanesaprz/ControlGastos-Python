from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QDate
from ui.gasto import Ui_dialogo_gasto

class DialogoMovimiento(QDialog):
    def __init__(self, tipo_movimiento):
        super().__init__()
        self.ui = Ui_dialogo_gasto()
        self.ui.setupUi(self)
        self.tipo_movimiento = tipo_movimiento

        self.configurar_por_tipo()

        self.ui.btn_guardar_gasto.clicked.connect(self.validar_aceptar)
        self.ui.btn_cancelar.clicked.connect(self.reject)



    def configurar_por_tipo(self):
        self.ui.fecha_gasto.setDate(QDate.currentDate())
        if self.tipo_movimiento == "ingreso":
            self.setWindowTitle("Nuevo Ingreso")
            self.ui.categoria_gasto.clear()
            lista_categoria = ["Selecciona una opción", "Nómina", "Honorarios", "Inversiones", "Extra", "Otros"]
            self.ui.categoria_gasto.addItems(lista_categoria)


        else:
            self.setWindowTitle("Nuevo Gasto")

    def validar_aceptar(self):
        descripcion = self.ui.descripcion_gasto.text().strip()
        categoria = self.ui.categoria_gasto.currentText()
        importe_txt = self.ui.importe_gasto.text().strip()

        if not descripcion:
            QMessageBox.warning(self, "Error", "Introduce una descripción")
            return
        if categoria == "Selecciona una opción":
            QMessageBox.warning(self, "Error", "Selecciona una categoría")
            return

        try:
            valor = abs(float(importe_txt.replace(',', '.')))
            self.importe_final = -valor if self.tipo_movimiento == "gasto" else valor
            self.accept()
        except ValueError:
            QMessageBox.warning(self, "Error", "El importe debe ser un número")

    def obtener_datos(self):
        #Diccionario de datos para introducir en la bbdd
        return {
            "fecha": self.ui.fecha_gasto.date().toPython(),
            "tipo": self.tipo_movimiento,
            "categoria": self.ui.categoria_gasto.currentText(),
            "descripcion": self.ui.descripcion_gasto.text(),
            "valor": self.importe_final
        }
