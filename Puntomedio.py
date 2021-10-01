import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "T2_Puntomedio.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.btn_calcular.clicked.connect(self.calcular)

    # Área de los Slots

    def calcular(self):

        x1 = self.txt_x1.text()
        x2 = self.txt_x2.text()
        y1 = self.txt_y1.text()
        y2 = self.txt_y2.text()

        x1 = int(x1)

        x2 = int(x2)

        y1 = int(y1)

        y2 = int(y2)

        x = x1 + x2

        x = x / 2

        y = y1 + y2

        y = y / 2

        self.txt_resultado.setText(str(x) + "," + str(y))

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())