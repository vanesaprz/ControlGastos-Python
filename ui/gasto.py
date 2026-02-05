# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gasto.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_dialogo_gasto(object):
    def setupUi(self, dialogo_gasto):
        if not dialogo_gasto.objectName():
            dialogo_gasto.setObjectName(u"dialogo_gasto")
        dialogo_gasto.resize(417, 316)
        self.label = QLabel(dialogo_gasto)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 50, 101, 21))
        self.descripcion_gasto = QLineEdit(dialogo_gasto)
        self.descripcion_gasto.setObjectName(u"descripcion_gasto")
        self.descripcion_gasto.setGeometry(QRect(110, 50, 291, 21))
        self.importe_gasto = QLineEdit(dialogo_gasto)
        self.importe_gasto.setObjectName(u"importe_gasto")
        self.importe_gasto.setGeometry(QRect(110, 130, 191, 21))
        self.label_2 = QLabel(dialogo_gasto)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 90, 71, 21))
        self.categoria_gasto = QComboBox(dialogo_gasto)
        self.categoria_gasto.addItem("")
        self.categoria_gasto.addItem("")
        self.categoria_gasto.addItem("")
        self.categoria_gasto.addItem("")
        self.categoria_gasto.addItem("")
        self.categoria_gasto.addItem("")
        self.categoria_gasto.addItem("")
        self.categoria_gasto.addItem("")
        self.categoria_gasto.addItem("")
        self.categoria_gasto.addItem("")
        self.categoria_gasto.setObjectName(u"categoria_gasto")
        self.categoria_gasto.setGeometry(QRect(110, 90, 281, 26))
        self.label_3 = QLabel(dialogo_gasto)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 130, 71, 21))
        self.label_4 = QLabel(dialogo_gasto)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 170, 56, 13))
        self.fecha_gasto = QDateTimeEdit(dialogo_gasto)
        self.fecha_gasto.setObjectName(u"fecha_gasto")
        self.fecha_gasto.setGeometry(QRect(110, 160, 201, 24))
        self.fecha_gasto.setDate(QDate(2026, 1, 1))
        self.fecha_gasto.setTime(QTime(0, 0, 0))
        self.fecha_gasto.setCalendarPopup(True)
        self.btn_guardar_gasto = QPushButton(dialogo_gasto)
        self.btn_guardar_gasto.setObjectName(u"btn_guardar_gasto")
        self.btn_guardar_gasto.setGeometry(QRect(270, 250, 110, 32))
        palette = QPalette()
        brush = QBrush(QColor(147, 105, 236, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        self.btn_guardar_gasto.setPalette(palette)
        self.btn_cancelar = QPushButton(dialogo_gasto)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(150, 250, 110, 32))

        self.retranslateUi(dialogo_gasto)

        QMetaObject.connectSlotsByName(dialogo_gasto)
    # setupUi

    def retranslateUi(self, dialogo_gasto):
        dialogo_gasto.setWindowTitle(QCoreApplication.translate("dialogo_gasto", u"Introduce los datos solicitados", None))
        self.label.setText(QCoreApplication.translate("dialogo_gasto", u"Descripci\u00f3n:", None))
        self.label_2.setText(QCoreApplication.translate("dialogo_gasto", u"Categor\u00eda: ", None))
        self.categoria_gasto.setItemText(0, QCoreApplication.translate("dialogo_gasto", u"Selecciona una opci\u00f3n", None))
        self.categoria_gasto.setItemText(1, QCoreApplication.translate("dialogo_gasto", u"Vivienda", None))
        self.categoria_gasto.setItemText(2, QCoreApplication.translate("dialogo_gasto", u"Alimentaci\u00f3n", None))
        self.categoria_gasto.setItemText(3, QCoreApplication.translate("dialogo_gasto", u"Transporte", None))
        self.categoria_gasto.setItemText(4, QCoreApplication.translate("dialogo_gasto", u"Facturas", None))
        self.categoria_gasto.setItemText(5, QCoreApplication.translate("dialogo_gasto", u"Salud", None))
        self.categoria_gasto.setItemText(6, QCoreApplication.translate("dialogo_gasto", u"Deudas", None))
        self.categoria_gasto.setItemText(7, QCoreApplication.translate("dialogo_gasto", u"Ocio", None))
        self.categoria_gasto.setItemText(8, QCoreApplication.translate("dialogo_gasto", u"Personal", None))
        self.categoria_gasto.setItemText(9, QCoreApplication.translate("dialogo_gasto", u"Otros", None))

        self.label_3.setText(QCoreApplication.translate("dialogo_gasto", u"Importe (\u20ac):", None))
        self.label_4.setText(QCoreApplication.translate("dialogo_gasto", u"Fecha:", None))
        self.fecha_gasto.setDisplayFormat(QCoreApplication.translate("dialogo_gasto", u"dd/MM/yyyy ", None))
        self.btn_guardar_gasto.setText(QCoreApplication.translate("dialogo_gasto", u"Guardar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("dialogo_gasto", u"Cancelar", None))
    # retranslateUi

