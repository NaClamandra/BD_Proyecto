from select_operacion import *
from operacion_create import *

class select_operacion(QtWidgets.QMainWindow, Ui_select_operacion):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = select_operacion()
    window.show()
    app.exec_()