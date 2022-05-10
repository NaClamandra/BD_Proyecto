# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consulta.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import psycopg2
import numpy
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_consultar(object):
    def setupUi(self, consultar):
        consultar.setObjectName("consultar")
        consultar.resize(794, 600)
        self.centralwidget = QtWidgets.QWidget(consultar)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 771, 531))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(30, 30, 111, 20))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(170, 30, 511, 491))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        consultar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(consultar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        consultar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(consultar)
        self.statusbar.setObjectName("statusbar")
        consultar.setStatusBar(self.statusbar)

        self.retranslateUi(consultar)
        QtCore.QMetaObject.connectSlotsByName(consultar)
        self.comboBox.setCurrentIndex(0)
        self.comboBox.currentTextChanged.connect(self.cambioCombo)

    def retranslateUi(self, consultar):
        _translate = QtCore.QCoreApplication.translate
        consultar.setWindowTitle(_translate("consultar", "MainWindow"))
        self.groupBox.setTitle(_translate("consultar", "GroupBox"))
        self.comboBox.setItemText(0, _translate("consultar", "--Tabla--"))
        self.comboBox.setItemText(1, _translate("consultar", "Ventas"))
        self.comboBox.setItemText(2, _translate("consultar", "Embotelladora"))
        self.comboBox.setItemText(3, _translate("consultar", "Ruta"))
        self.comboBox.setItemText(4, _translate("consultar", "Repartidor"))
        self.comboBox.setItemText(5, _translate("consultar", "Local"))
        self.comboBox.setItemText(6, _translate("consultar", "Genera"))

    def cambioCombo(self):
        try:
            conn = psycopg2.connect(
                database="embotelladoras",
                user="postgres",
                password="3328764133"
            )
            print("ñonga")
        except psycopg2.Error as e:
            print(e)
        cur = conn.cursor()
        try:
            row_count = 0
            column_count = 0
            table = self.comboBox.currentText().lower()
            names_query = f"select column_name from information_schema.columns where table_name = '{table}'"
            cur.execute(names_query)
            result_names_query = cur.fetchall()
            names_list = list(map(lambda x: x[0], result_names_query))
            column_count = len(result_names_query)
            data_query = f"select * from {table}"
            cur.execute(data_query)
            result_data_query = cur.fetchall()
            data_list = list(result_data_query)
            row_count = len(result_data_query)
            self.tableWidget.setRowCount(row_count)
            self.tableWidget.setColumnCount(column_count)
            self.tableWidget.setHorizontalHeaderLabels(names_list)
            fila = row_count - 1
            f = 0
            columna = column_count - 1
            c = 0
            for row in range(row_count):
                for col in range(column_count):
                    self.tableWidget.setItem(f, c, QtWidgets.QTableWidgetItem(str(data_list[f][c])))
                    c += 1
                c = 0
                f += 1
            self.tableWidget.setEnabled(False)
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
            ##self.tableWidget.resizeRowsToContents()
        except psycopg2.Error as e:
            print(e)
        conn.commit()
        cur.close()
        conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    consultar = QtWidgets.QMainWindow()
    ui = Ui_consultar()
    ui.setupUi(consultar)
    consultar.show()
    sys.exit(app.exec_())

