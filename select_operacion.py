from consulta import *
from operacion_create import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_select_operacion(object):
    def setupUi(self, select_operacion):
        self.Ui_operacion = Ui_operacion()
        select_operacion.setObjectName("select_operacion")
        select_operacion.resize(389, 372)
        self.centralwidget = QtWidgets.QWidget(select_operacion)
        self.centralwidget.setObjectName("centralwidget")

        self.create = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openCreate())
        self.create.setGeometry(QtCore.QRect(40, 30, 111, 41))
        self.create.setObjectName("create")

        self.read = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openConsulta())
        self.read.setGeometry(QtCore.QRect(210, 30, 111, 41))
        self.read.setObjectName("read")

        self.update = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openUpdate())
        self.update.setGeometry(QtCore.QRect(40, 110, 111, 41))
        self.update.setObjectName("update")

        self.delete_ = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openDelete())
        self.delete_.setGeometry(QtCore.QRect(210, 110, 111, 41))
        self.delete_.setObjectName("delete_")

        select_operacion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(select_operacion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 389, 21))
        self.menubar.setObjectName("menubar")
        select_operacion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(select_operacion)
        self.statusbar.setObjectName("statusbar")
        select_operacion.setStatusBar(self.statusbar)

        self.retranslateUi(select_operacion)
        QtCore.QMetaObject.connectSlotsByName(select_operacion)

    def retranslateUi(self, select_operacion):
        _translate = QtCore.QCoreApplication.translate
        select_operacion.setWindowTitle(_translate("select_operacion", "MainWindow"))
        self.create.setText(_translate("select_operacion", "Nuevo"))
        self.read.setText(_translate("select_operacion", "Consultar"))
        self.update.setText(_translate("select_operacion", "Modificar"))
        self.delete_.setText(_translate("select_operacion", "Eliminar"))

    def openCreate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_operacion()
        self.ui.setupUi(self.window)
        self.ui.secreto.setText("insert")
        self.window.setWindowTitle("Create")
        self.window.show()

    def openDelete(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_operacion()
        self.ui.setupUi(self.window)
        self.ui.secreto.setText("delete")
        self.window.setWindowTitle("Delete")
        self.window.show()

    def openUpdate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_operacion()
        self.ui.setupUi(self.window)
        self.ui.secreto.setText("update")
        self.window.setWindowTitle("Update")
        self.window.show()

    def openConsulta(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_consultar()
        self.ui.setupUi(self.window)
        self.window.setWindowTitle("Read")
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_operacion = QtWidgets.QMainWindow()
    ui = Ui_select_operacion()
    ui.setupUi(select_operacion)
    select_operacion.show()
    sys.exit(app.exec_())

