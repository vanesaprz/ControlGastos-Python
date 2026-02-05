# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_1.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(827, 572)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.action_NuevoIngreso = QAction(MainWindow)
        self.action_NuevoIngreso.setObjectName(u"action_NuevoIngreso")
        self.actionNueva_meta = QAction(MainWindow)
        self.actionNueva_meta.setObjectName(u"actionNueva_meta")
        self.actionPrincipal = QAction(MainWindow)
        self.actionPrincipal.setObjectName(u"actionPrincipal")
        self.action_VerInformes = QAction(MainWindow)
        self.action_VerInformes.setObjectName(u"action_VerInformes")
        self.actionMetas = QAction(MainWindow)
        self.actionMetas.setObjectName(u"actionMetas")
        self.actionCrear_informe = QAction(MainWindow)
        self.actionCrear_informe.setObjectName(u"actionCrear_informe")
        self.action_NuevoGasto = QAction(MainWindow)
        self.action_NuevoGasto.setObjectName(u"action_NuevoGasto")
        self.actionInformes = QAction(MainWindow)
        self.actionInformes.setObjectName(u"actionInformes")
        self.actionVer_informes = QAction(MainWindow)
        self.actionVer_informes.setObjectName(u"actionVer_informes")
        self.actionTablero_Principal = QAction(MainWindow)
        self.actionTablero_Principal.setObjectName(u"actionTablero_Principal")
        self.actionVerInformes = QAction(MainWindow)
        self.actionVerInformes.setObjectName(u"actionVerInformes")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(190, 0, 641, 521))
        self.w_tablero_principal = QWidget()
        self.w_tablero_principal.setObjectName(u"w_tablero_principal")
        self.verticalLayoutWidget_2 = QWidget(self.w_tablero_principal)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 0, 611, 521))
        self.layout_principal = QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_principal.setObjectName(u"layout_principal")
        self.layout_principal.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_principal.addItem(self.horizontalSpacer)

        self.nombre_tablero = QLabel(self.verticalLayoutWidget_2)
        self.nombre_tablero.setObjectName(u"nombre_tablero")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.nombre_tablero.setFont(font)
        self.nombre_tablero.setTextFormat(Qt.RichText)
        self.nombre_tablero.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)

        self.layout_principal.addWidget(self.nombre_tablero)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout_principal.addItem(self.horizontalSpacer_2)

        self.balance_tablero = QLabel(self.verticalLayoutWidget_2)
        self.balance_tablero.setObjectName(u"balance_tablero")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        self.balance_tablero.setFont(font1)

        self.layout_principal.addWidget(self.balance_tablero)

        self.resumen_dinero = QLabel(self.verticalLayoutWidget_2)
        self.resumen_dinero.setObjectName(u"resumen_dinero")
        font2 = QFont()
        font2.setPointSize(19)
        self.resumen_dinero.setFont(font2)
        self.resumen_dinero.setAlignment(Qt.AlignCenter)

        self.layout_principal.addWidget(self.resumen_dinero)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.layout_principal.addWidget(self.label)

        self.movimientos_tabla = QTableWidget(self.verticalLayoutWidget_2)
        if (self.movimientos_tabla.columnCount() < 5):
            self.movimientos_tabla.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.movimientos_tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.movimientos_tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.movimientos_tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.movimientos_tabla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.movimientos_tabla.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.movimientos_tabla.setObjectName(u"movimientos_tabla")
        self.movimientos_tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.movimientos_tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.layout_principal.addWidget(self.movimientos_tabla)

        self.btn_ingreso = QPushButton(self.verticalLayoutWidget_2)
        self.btn_ingreso.setObjectName(u"btn_ingreso")

        self.layout_principal.addWidget(self.btn_ingreso)

        self.btn_gasto = QPushButton(self.verticalLayoutWidget_2)
        self.btn_gasto.setObjectName(u"btn_gasto")

        self.layout_principal.addWidget(self.btn_gasto)

        self.eliminar_seleccion = QPushButton(self.verticalLayoutWidget_2)
        self.eliminar_seleccion.setObjectName(u"eliminar_seleccion")

        self.layout_principal.addWidget(self.eliminar_seleccion)

        self.stackedWidget.addWidget(self.w_tablero_principal)
        self.w_movimientos = QWidget()
        self.w_movimientos.setObjectName(u"w_movimientos")
        self.horizontalLayoutWidget = QWidget(self.w_movimientos)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 621, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.combo_informes = QComboBox(self.horizontalLayoutWidget)
        self.combo_informes.addItem("")
        self.combo_informes.addItem("")
        self.combo_informes.addItem("")
        self.combo_informes.addItem("")
        self.combo_informes.setObjectName(u"combo_informes")

        self.horizontalLayout.addWidget(self.combo_informes)

        self.btn_gen_informes = QPushButton(self.horizontalLayoutWidget)
        self.btn_gen_informes.setObjectName(u"btn_gen_informes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_gen_informes.sizePolicy().hasHeightForWidth())
        self.btn_gen_informes.setSizePolicy(sizePolicy1)
        self.btn_gen_informes.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.btn_gen_informes)

        self.verticalLayoutWidget = QWidget(self.w_movimientos)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 50, 621, 461))
        self.html_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.html_layout.setObjectName(u"html_layout")
        self.html_layout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.w_movimientos)
        self.b_informes = QPushButton(self.centralwidget)
        self.b_informes.setObjectName(u"b_informes")
        self.b_informes.setGeometry(QRect(10, 80, 171, 61))
        self.b_tablero = QPushButton(self.centralwidget)
        self.b_tablero.setObjectName(u"b_tablero")
        self.b_tablero.setGeometry(QRect(10, 20, 171, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 827, 30))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVentana = QMenu(self.menubar)
        self.menuVentana.setObjectName(u"menuVentana")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVentana.menuAction())
        self.menuArchivo.addAction(self.action_NuevoIngreso)
        self.menuArchivo.addAction(self.action_NuevoGasto)
        self.menuVentana.addAction(self.actionTablero_Principal)
        self.menuVentana.addAction(self.actionVerInformes)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"App Control Gastos", None))
        self.action_NuevoIngreso.setText(QCoreApplication.translate("MainWindow", u"Nuevo ingreso", None))
#if QT_CONFIG(shortcut)
        self.action_NuevoIngreso.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionNueva_meta.setText(QCoreApplication.translate("MainWindow", u"Nueva meta", None))
        self.actionPrincipal.setText(QCoreApplication.translate("MainWindow", u"Tablero", None))
        self.action_VerInformes.setText(QCoreApplication.translate("MainWindow", u"Informes", None))
        self.actionMetas.setText(QCoreApplication.translate("MainWindow", u"Metas", None))
        self.actionCrear_informe.setText(QCoreApplication.translate("MainWindow", u"Crear informe", None))
        self.action_NuevoGasto.setText(QCoreApplication.translate("MainWindow", u"Nuevo gasto", None))
#if QT_CONFIG(shortcut)
        self.action_NuevoGasto.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+G", None))
#endif // QT_CONFIG(shortcut)
        self.actionInformes.setText(QCoreApplication.translate("MainWindow", u"Informes", None))
        self.actionVer_informes.setText(QCoreApplication.translate("MainWindow", u"Ver informes", None))
#if QT_CONFIG(shortcut)
        self.actionVer_informes.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+Shift+G", None))
#endif // QT_CONFIG(shortcut)
        self.actionTablero_Principal.setText(QCoreApplication.translate("MainWindow", u"Tablero Principal", None))
#if QT_CONFIG(shortcut)
        self.actionTablero_Principal.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionVerInformes.setText(QCoreApplication.translate("MainWindow", u"Informes", None))
#if QT_CONFIG(shortcut)
        self.actionVerInformes.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.nombre_tablero.setText(QCoreApplication.translate("MainWindow", u"MI TABLERO PRINCIPAL", None))
        self.balance_tablero.setText(QCoreApplication.translate("MainWindow", u"BALANCE (\u20ac) : ", None))
        self.resumen_dinero.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MIS MOVIMIENTOS", None))
        ___qtablewidgetitem = self.movimientos_tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.movimientos_tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem2 = self.movimientos_tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None));
        ___qtablewidgetitem3 = self.movimientos_tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None));
        ___qtablewidgetitem4 = self.movimientos_tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Importe", None));
        self.btn_ingreso.setText(QCoreApplication.translate("MainWindow", u" A\u00f1adir ingreso", None))
        self.btn_gasto.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir gasto", None))
        self.eliminar_seleccion.setText(QCoreApplication.translate("MainWindow", u"Eliminar seleccionado", None))
        self.combo_informes.setItemText(0, QCoreApplication.translate("MainWindow", u"\u00daltimos 30 d\u00edas", None))
        self.combo_informes.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00daltimos 6 meses", None))
        self.combo_informes.setItemText(2, QCoreApplication.translate("MainWindow", u"\u00daltimo a\u00f1o", None))
        self.combo_informes.setItemText(3, QCoreApplication.translate("MainWindow", u"Todos los tiempos", None))

        self.btn_gen_informes.setText(QCoreApplication.translate("MainWindow", u"Generar informe", None))
        self.b_informes.setText(QCoreApplication.translate("MainWindow", u"Informes", None))
        self.b_tablero.setText(QCoreApplication.translate("MainWindow", u"Tablero Principal", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVentana.setTitle(QCoreApplication.translate("MainWindow", u"Ventana", None))
    # retranslateUi

