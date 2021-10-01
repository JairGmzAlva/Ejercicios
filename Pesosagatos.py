import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "T4_Pesosagatos.ui" # Nombre del archivo aquí.

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

        num = self.txt_num.text()

        if (num == ""):

            self.txt_resultado.setText("Ingresa un valor")

        else:

            num = int(num)

        if(num >= 5):

            num = num / 5

            self.txt_resultado.setText(str(num))

        else:

            self.txt_resultado.setText("Se redondea a 1 gato")

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())