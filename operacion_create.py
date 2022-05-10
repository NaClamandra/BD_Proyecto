# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'operacion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

class Ui_operacion(object):
    def setupUi(self, operacion):
        operacion.setObjectName("operacion")
        operacion.resize(572, 400)
        self.centralwidget = QtWidgets.QWidget(operacion)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.secreto = QtWidgets.QLabel(self.groupBox)
        self.secreto.setEnabled(False)
        self.secreto.setVisible(False)
        self.secreto.setGeometry(QtCore.QRect(30, 70, 281, 32))
        self.secreto.setObjectName("secreto")

####    Ruta
        self.dia_circ_ruta = QtWidgets.QPlainTextEdit(self.groupBox)
        self.dia_circ_ruta.setEnabled(False)
        self.dia_circ_ruta.setVisible(False)
        self.dia_circ_ruta.setGeometry(QtCore.QRect(30, 70, 281, 32))
        self.dia_circ_ruta.setObjectName("dia_circ_ruta")

        self.kilometros_ruta = QtWidgets.QPlainTextEdit(self.groupBox)
        self.kilometros_ruta.setEnabled(False)
        self.kilometros_ruta.setVisible(False)
        self.kilometros_ruta.setGeometry(QtCore.QRect(30, 20, 281, 32))
        self.kilometros_ruta.setObjectName("kilometros_ruta")

        self.cod_rep_ruta = QtWidgets.QPlainTextEdit(self.groupBox)
        self.cod_rep_ruta.setEnabled(False)
        self.cod_rep_ruta.setVisible(False)
        self.cod_rep_ruta.setGeometry(QtCore.QRect(30, 120, 281, 33))
        self.cod_rep_ruta.setObjectName("cod_rep_ruta")

####    Local
        self.cant_prod_local = QtWidgets.QPlainTextEdit(self.groupBox)
        self.cant_prod_local.setEnabled(False)
        self.cant_prod_local.setVisible(False)
        self.cant_prod_local.setGeometry(QtCore.QRect(30, 120, 281, 33))
        self.cant_prod_local.setObjectName("cant_prod_local")

        self.direccion_local = QtWidgets.QPlainTextEdit(self.groupBox)
        self.direccion_local.setEnabled(False)
        self.direccion_local.setVisible(False)
        self.direccion_local.setGeometry(QtCore.QRect(30, 20, 281, 32))
        self.direccion_local.setObjectName("direccion_local")

        self.no_ruta_local = QtWidgets.QPlainTextEdit(self.groupBox)
        self.no_ruta_local.setEnabled(False)
        self.no_ruta_local.setVisible(False)
        self.no_ruta_local.setGeometry(QtCore.QRect(30, 70, 281, 33))
        self.no_ruta_local.setObjectName("no_ruta_local")

        self.nombre_local = QtWidgets.QPlainTextEdit(self.groupBox)
        self.nombre_local.setEnabled(False)
        self.nombre_local.setVisible(False)
        self.nombre_local.setGeometry(QtCore.QRect(30, 170, 281, 32))
        self.nombre_local.setObjectName("nombre_local")

####    Embotelladora
        self.nombre_embotelladora = QtWidgets.QPlainTextEdit(self.groupBox)
        self.nombre_embotelladora.setEnabled(False)
        self.nombre_embotelladora.setVisible(False)
        self.nombre_embotelladora.setGeometry(QtCore.QRect(30, 70, 281, 31))
        self.nombre_embotelladora.setObjectName("nombre_embotelladora")

        self.direccion_embotelladora = QtWidgets.QPlainTextEdit(self.groupBox)
        self.direccion_embotelladora.setEnabled(False)
        self.direccion_embotelladora.setVisible(False)
        self.direccion_embotelladora.setGeometry(QtCore.QRect(30, 23, 281, 33))
        self.direccion_embotelladora.setObjectName("direccion_embotelladora")

####    Repartidor
        self.sueldo_repartidor = QtWidgets.QPlainTextEdit(self.groupBox)
        self.sueldo_repartidor.setEnabled(False)
        self.sueldo_repartidor.setVisible(False)
        self.sueldo_repartidor.setGeometry(QtCore.QRect(30, 70, 281, 33))
        self.sueldo_repartidor.setObjectName("sueldo_repartidor")

        self.fech_nac_repartidor = QtWidgets.QPlainTextEdit(self.groupBox)
        self.fech_nac_repartidor.setEnabled(False)
        self.fech_nac_repartidor.setVisible(False)
        self.fech_nac_repartidor.setGeometry(QtCore.QRect(30, 120, 281, 32))
        self.fech_nac_repartidor.setObjectName("fech_nac_repartidor")

        self.cod_emb_repartidor = QtWidgets.QPlainTextEdit(self.groupBox)
        self.cod_emb_repartidor.setEnabled(False)
        self.cod_emb_repartidor.setVisible(False)
        self.cod_emb_repartidor.setGeometry(QtCore.QRect(30, 170, 281, 33))
        self.cod_emb_repartidor.setObjectName("cod_emb_repartidor")

        self.nombre_repartidor = QtWidgets.QPlainTextEdit(self.groupBox)
        self.nombre_repartidor.setEnabled(False)
        self.nombre_repartidor.setVisible(False)
        self.nombre_repartidor.setGeometry(QtCore.QRect(30, 20, 281, 32))
        self.nombre_repartidor.setObjectName("nombre_repartidor")

####    Ventas
        self.cod_ven_ventas = QtWidgets.QPlainTextEdit(self.groupBox)
        self.cod_ven_ventas.setEnabled(False)
        self.cod_ven_ventas.setVisible(False)
        self.cod_ven_ventas.setGeometry(QtCore.QRect(30, 20, 281, 33))
        self.cod_ven_ventas.setObjectName("cod_ven_ventas")

        self.total_ventas = QtWidgets.QPlainTextEdit(self.groupBox)
        self.total_ventas.setEnabled(False)
        self.total_ventas.setVisible(False)
        self.total_ventas.setGeometry(QtCore.QRect(30, 70, 281, 33))
        self.total_ventas.setObjectName("total_ventas")

        self.fecha_ventas = QtWidgets.QPlainTextEdit(self.groupBox)
        self.fecha_ventas.setEnabled(False)
        self.fecha_ventas.setVisible(False)
        self.fecha_ventas.setGeometry(QtCore.QRect(30, 120, 281, 33))
        self.fecha_ventas.setObjectName("fecha_ventas")

        self.can_prod_ventas = QtWidgets.QPlainTextEdit(self.groupBox)
        self.can_prod_ventas.setEnabled(False)
        self.can_prod_ventas.setVisible(False)
        self.can_prod_ventas.setGeometry(QtCore.QRect(30, 170, 281, 33))
        self.can_prod_ventas.setObjectName("can_prod_ventas")

        self.cod_rep_ventas = QtWidgets.QPlainTextEdit(self.groupBox)
        self.cod_rep_ventas.setEnabled(False)
        self.cod_rep_ventas.setVisible(False)
        self.cod_rep_ventas.setGeometry(QtCore.QRect(30, 220, 281, 33))
        self.cod_rep_ventas.setObjectName("cod_rep_ventas")

        self.nom_loc_ventas = QtWidgets.QPlainTextEdit(self.groupBox)
        self.nom_loc_ventas.setEnabled(False)
        self.nom_loc_ventas.setVisible(False)
        self.nom_loc_ventas.setGeometry(QtCore.QRect(30, 270, 281, 32))
        self.nom_loc_ventas.setObjectName("nom_loc_ventas")

        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(400, 30, 91, 20))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.ejecutar = QtWidgets.QPushButton(self.groupBox)
        self.ejecutar.setEnabled(True)
        self.ejecutar.setGeometry(QtCore.QRect(400, 90, 91, 23))
        self.ejecutar.setObjectName("ejecutar")

        self.limpiar = QtWidgets.QPushButton(self.groupBox)
        self.limpiar.setEnabled(True)
        self.limpiar.setGeometry(QtCore.QRect(400, 130, 91, 23))
        self.limpiar.setObjectName("limpiar")

        self.horizontalLayout.addWidget(self.groupBox)
        operacion.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(operacion)
        self.statusbar.setObjectName("statusbar")
        operacion.setStatusBar(self.statusbar)

        self.retranslateUi(operacion)
        QtCore.QMetaObject.connectSlotsByName(operacion)
        self.comboBox.currentTextChanged.connect(self.changeTable)
        self.ejecutar.clicked.connect(self.ejecuta)
        self.comboBox.setCurrentIndex(0)


    def retranslateUi(self, operacion):
        _translate = QtCore.QCoreApplication.translate
        operacion.setWindowTitle(_translate("operacion", "MainWindow"))
        self.dia_circ_ruta.setPlaceholderText(_translate("operacion", "Dias de circulación"))
        self.cant_prod_local.setPlaceholderText(_translate("operacion", "Cantidad de producto"))
        self.direccion_local.setPlaceholderText(_translate("operacion", "Direccion del local"))
        self.kilometros_ruta.setPlaceholderText(_translate("operacion", "Kilometros de ruta"))
        self.cod_emb_repartidor.setPlaceholderText(_translate("operacion", "Codigo de embotelladora"))
        self.no_ruta_local.setPlaceholderText(_translate("operacion", "N° de ruta"))
        self.nombre_embotelladora.setPlaceholderText(_translate("operacion", "Nombre de embotelladora"))
        self.sueldo_repartidor.setPlaceholderText(_translate("operacion", "sueldo del repartidor"))
        self.fech_nac_repartidor.setPlaceholderText(_translate("operacion", "Fecha de nacimiento"))
        self.direccion_embotelladora.setPlaceholderText(_translate("operacion", "Direccion de embotelladora"))
        self.nombre_local.setPlaceholderText(_translate("operacion", "Nombre del local"))
        self.nombre_repartidor.setPlaceholderText(_translate("operacion", "Nombre del repartidor"))
        self.comboBox.setItemText(0, _translate("operacion", "--Tabla--"))
        self.comboBox.setItemText(1, _translate("operacion", "Ventas"))
        self.comboBox.setItemText(2, _translate("operacion", "Embotelladora"))
        self.comboBox.setItemText(3, _translate("operacion", "Ruta"))
        self.comboBox.setItemText(4, _translate("operacion", "Repartidor"))
        self.comboBox.setItemText(5, _translate("operacion", "Local"))
        self.cod_rep_ruta.setPlaceholderText(_translate("operacion", "Codigo de repartidor"))
        self.cod_ven_ventas.setPlaceholderText(_translate("operacion", "Codigo de venta"))
        self.total_ventas.setPlaceholderText(_translate("operacion", "Total de la venta"))
        self.fecha_ventas.setPlaceholderText(_translate("operacion", "Fecha de la venta"))
        self.can_prod_ventas.setPlaceholderText(_translate("operacion", "Cantidad de producto"))
        self.cod_rep_ventas.setPlaceholderText(_translate("operacion", "Codigo de repartidor"))
        self.nom_loc_ventas.setPlaceholderText(_translate("operacion", "Nombre del local"))
        self.ejecutar.setText(_translate("operacion", "Procesar"))
        self.limpiar.setText(_translate("operacion", "Limpiar"))

    def changeTable(self):
        table = self.comboBox.currentText().lower()
        if(table == 'ruta'):
            self.disableAll()
            self.dia_circ_ruta.setEnabled(True)
            self.dia_circ_ruta.setVisible(True)

            self.kilometros_ruta.setEnabled(True)
            self.kilometros_ruta.setVisible(True)

            self.cod_rep_ruta.setEnabled(True)
            self.cod_rep_ruta.setVisible(True)

        if(table == 'ventas'):
            self.disableAll()
            self.cod_ven_ventas.setEnabled(True)
            self.cod_ven_ventas.setVisible(True)

            self.total_ventas.setEnabled(True)
            self.total_ventas.setVisible(True)

            self.fecha_ventas.setEnabled(True)
            self.fecha_ventas.setVisible(True)

            self.can_prod_ventas.setEnabled(True)
            self.can_prod_ventas.setVisible(True)

            self.cod_rep_ventas.setEnabled(True)
            self.cod_rep_ventas.setVisible(True)

            self.nom_loc_ventas.setEnabled(True)
            self.nom_loc_ventas.setVisible(True)

        if(table == 'embotelladora'):
            self.disableAll()
            self.nombre_embotelladora.setEnabled(True)
            self.nombre_embotelladora.setVisible(True)

            self.direccion_embotelladora.setEnabled(True)
            self.direccion_embotelladora.setVisible(True)

        if(table == 'local'):
            self.disableAll()
            self.cant_prod_local.setEnabled(True)
            self.cant_prod_local.setVisible(True)

            self.direccion_local.setEnabled(True)
            self.direccion_local.setVisible(True)

            self.no_ruta_local.setEnabled(True)
            self.no_ruta_local.setVisible(True)

            self.nombre_local.setEnabled(True)
            self.nombre_local.setVisible(True)

        if(table == 'repartidor'):
            self.disableAll()
            self.sueldo_repartidor.setEnabled(True)
            self.sueldo_repartidor.setVisible(True)

            self.fech_nac_repartidor.setEnabled(True)
            self.fech_nac_repartidor.setVisible(True)

            self.cod_emb_repartidor.setEnabled(True)
            self.cod_emb_repartidor.setVisible(True)

            self.nombre_repartidor.setEnabled(True)
            self.nombre_repartidor.setVisible(True)

    def ejecuta(self):
        table = self.comboBox.currentText().lower()
        op = str(self.secreto.text())
        bien = True
        if (table == 'ruta'):
            kilometros = self.kilometros_ruta.toPlainText()
            dias = self.dia_circ_ruta.toPlainText()
            cod_r = self.cod_rep_ruta.toPlainText()
            if(kilometros == ""):
                bien = False
            if(dias == ""):
                bien = False
            if(cod_r == ""):
                bien = False
            if(bien == True):
                try:
                    conn = psycopg2.connect(
                        database="embotelladoras",
                        user="postgres",
                        password="3328764133"
                    )
                except psycopg2.Error as e:
                    print(e)
                cur = conn.cursor()
                try:
                    insert_query = f"{op} into {table} (kilometros, dias_circulacion, codigo_repartidor) values({kilometros},'{dias}',{cod_r})"
                    cur.execute(insert_query)
                except psycopg2.Error as e:
                    print(e)
                conn.commit()
                cur.close()
                conn.close()

        if (table == 'ventas'):
            kilometros = self.kilometros_ruta.toPlainText()
            dias = self.dia_circ_ruta.toPlainText()
            cod_r = self.cod_rep_ruta.toPlainText()
            if(kilometros == ""):
                bien = False
            if(dias == ""):
                bien = False
            if(cod_r == ""):
                bien = False
            if(bien == True):
                try:
                    conn = psycopg2.connect(
                        database="embotelladoras",
                        user="postgres",
                        password="3328764133"
                    )
                except psycopg2.Error as e:
                    print(e)
                cur = conn.cursor()
                try:
                    insert_query = f"{op} into {table} (kilometros, dias_circulacion, codigo_repartidor) values({kilometros},'{dias}',{cod_r})"
                    cur.execute(insert_query)
                except psycopg2.Error as e:
                    print(e)
                conn.commit()
                cur.close()
                conn.close()

        if (table == 'embotelladora'):
            nombre = self.nombre_embotelladora.toPlainText()
            direccion = self.direccion_embotelladora.toPlainText()
            if (nombre == ""):
                bien = False
            if (direccion == ""):
                bien = False
            if (bien == True):
                try:
                    conn = psycopg2.connect(
                        database="embotelladoras",
                        user="postgres",
                        password="3328764133"
                    )
                    print("pinga")
                except psycopg2.Error as e:
                    print(e)
                cur = conn.cursor()
                try:
                    insert_query = f"{op} into {table} (nombre, direccion) values('{nombre}','{direccion}')"
                    cur.execute(insert_query)
                    print("hecho")
                except psycopg2.Error as e:
                    print(e)
                conn.commit()
                cur.close()
                conn.close()

     #   if (table == 'local'):


       # if (table == 'repartidor'):


    def disableAll(self):
        self.dia_circ_ruta.setEnabled(False)
        self.dia_circ_ruta.setVisible(False)

        self.kilometros_ruta.setEnabled(False)
        self.kilometros_ruta.setVisible(False)

        self.cod_rep_ruta.setEnabled(False)
        self.cod_rep_ruta.setVisible(False)

        self.cant_prod_local.setEnabled(False)
        self.cant_prod_local.setVisible(False)

        self.direccion_local.setEnabled(False)
        self.direccion_local.setVisible(False)

        self.no_ruta_local.setEnabled(False)
        self.no_ruta_local.setVisible(False)

        self.nombre_local.setEnabled(False)
        self.nombre_local.setVisible(False)

        self.nombre_embotelladora.setEnabled(False)
        self.nombre_embotelladora.setVisible(False)

        self.direccion_embotelladora.setEnabled(False)
        self.direccion_embotelladora.setVisible(False)

        self.sueldo_repartidor.setEnabled(False)
        self.sueldo_repartidor.setVisible(False)

        self.fech_nac_repartidor.setEnabled(False)
        self.fech_nac_repartidor.setVisible(False)

        self.cod_emb_repartidor.setEnabled(False)
        self.cod_emb_repartidor.setVisible(False)

        self.nombre_repartidor.setEnabled(False)
        self.nombre_repartidor.setVisible(False)

        self.cod_ven_ventas.setEnabled(False)
        self.cod_ven_ventas.setVisible(False)

        self.total_ventas.setEnabled(False)
        self.total_ventas.setVisible(False)

        self.fecha_ventas.setEnabled(False)
        self.fecha_ventas.setVisible(False)

        self.can_prod_ventas.setEnabled(False)
        self.can_prod_ventas.setVisible(False)

        self.cod_rep_ventas.setEnabled(False)
        self.cod_rep_ventas.setVisible(False)

        self.nom_loc_ventas.setEnabled(False)
        self.nom_loc_ventas.setVisible(False)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    operacion = QtWidgets.QMainWindow()
    ui = Ui_operacion()
    ui.setupUi(operacion)
    operacion.show()
    sys.exit(app.exec_())

