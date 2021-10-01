import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P1_5_DistanciaEuclidiana.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # AREA DE LOS SIGNALS

        self.btn_operacion.clicked.connect(self.operacion) #BOTON OPERACION SE ENLAZA CON OPERACION

        self.btn_operacion.setText("COMENZAR") #BOTON OPERACION EMPIEZA "COMENZAR"

        self.txt_vector1.setEnabled(False) #CUADRO DE TEXTO VECTOR1 EMPIEZA BLOQUEADO

        self.txt_vector2.setEnabled(False) #CUADRO DE TEXTO VECTOR2 EMPIEZA BLOQUEADO

        self.txt_pos_actual.setEnabled(False) #CUADRO DE TEXTO POS_ACTUAL EMPIEZA BLOQUEADO

        self.txt_resultado.setEnabled(False) #CUADRO DE TEXTO RESULTADO EMPIEZA BLOQUEADO

        self.n =- 1 #DECLARAMOS N = -1

        self.lista = [] #LISTA VACIA

    # AREA DE LOS SLOTS

    def operacion (self):

        op = self.btn_operacion.text() #OP ES IGUAL A ACCION DEL BOTON OPERACION

        if op == "COMENZAR": #SI OP ES IGUAL A COMENZAR

            self.txt_resultado.setText("") #CUADRO DE TEXTO RESULTADO SE LIMPIA

            self.btn_operacion.setText("AÑADIR") #EL BOTON OPERACION SE CAMBIA A AÑADIR

            self.n = int(self.txt_valores_por_vector.text()) #N ES IGUAL A EL VALOR INGRESADO EN EL CUADRO DE TEXTO VALORES_POR_VECTOR

            self.txt_vector1.setEnabled(True) #CUADRO DE TEXTO VECTOR1 SE HABILITA

            self.txt_vector2.setEnabled(True) #CUADRO DE TEXTO VECTOR2 SE HABILITA

            self.txt_pos_actual.setText("1") #CUADRO DE TEXTO POS_ACTUAL = 1

            self.txt_valores_por_vector.setEnabled(False) #CUADRO DE TEXTO VALORES_POR_VECTOR SE BLOQUEA

        elif op == "AÑADIR": #SI OP ES IGUAL A "AÑADIR"

            pos_actual = int(self.txt_pos_actual.text()) #POS_ACTUAL ES IGUAL A 1

            if pos_actual <= self.n: #SI POS_ACTUAL ES MENOR O IGUAL A N

                vector1 = int(self.txt_vector1.text()) #VECTOR1 ES IGUAL A EL VALOR INGRESADO EN EL CUADRO DE TEXTO VECTOR1

                vector2 = int(self.txt_vector2.text()) #VECTOR2 ES IGUAL A EL VALOR INGRESADO EN EL CUADRO DE TEXTO VECTOR2

                self.txt_vector1.setText("") #SE LIMPIA EL CUADRO DE TEXTO VECTOR1

                self.txt_vector2.setText("") #SE LIMPIA EL CUADRO DE TEXTO VECTOR2

                self.lista.append((vector1 - vector2) * (vector1 - vector2)) #ALGORITMO DE LA DIFERENCIA ENTRE EL VALOR DEL VECTOR1 Y EL VECTOR2 AL CUADRADO
                #LA DIFERENCIA AL CUADRADO SE GUARDA EN LA LISTA

                pos_actual += 1 #POS_ACTUAL MAS 1

                if pos_actual == self.n+1: #SI POS_ACTUAL ES IGUAL A N+1

                    self.btn_operacion.setText("CALCULAR") #EL BOTON OPERACION SE CAMBIA A "CALCULAR"

                    self.txt_vector1.setEnabled(False) #EL CUADRO DE TEXTO VECTOR1 SE BLOQUEA

                    self.txt_vector2.setEnabled(False) #EL CUADRO DE TEXTO VECTOR2 SE BLOQUEA

                else: #SI POS_ACTUAL NO ES IGUAL A N+1

                    self.txt_pos_actual.setText(str(pos_actual)) #EL CUADRO DE TEXTO POS_ACTUAL CAMBIA AL VALOR QUE CONTENGA POS_ACTUAL

        else: #SI OP ES IGUAL A CALCULAR

            self.btn_operacion.setText("COMENZAR") #EL BOTON OPERACION SE CAMBIA A "COMENZAR"

            suma = sum(self.lista) #SUMA ES IGUAL A LA SUMA DE LOS VALORES DE LA LISTA

            self.txt_resultado.setText(str(suma)) #EL CUADRO DE TEXTO RESULTADO CAMBIA AL VALOR DE LA VARIABLE SUMA

            self.lista.clear() #SE LIMPIA LA LISTA PARA REUTILIZAR EL PROYECTO

            self.txt_valores_por_vector.setEnabled(True) #EL CUADRO DE TEXTO VALORES_POR_VECTOR SE HABILITA

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())