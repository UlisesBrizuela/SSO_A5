#ACTIVIDAD 5 - SEMINARIO DE SOLUCION DE PROBLEMAS DE SISTEMAS OPERATIVOS
#BRIZUELA ARIAS ULISES ISRAEL

from PyQt5 import QtCore, QtGui, QtWidgets
from collections import deque
import sys

class Ui_MainWindow(object):

    def __init__(self) -> None:
        self.memoria = [[1000], [400], [1800], [700], [900], [1200], [1500]]
        self.procesos = []
        self.indice = 0

    def archivo(self):
        with open('./archivos.txt', 'r') as archivos:
            for archivo in archivos.readlines():
                nombre, tamaño = archivo.strip().split(',')
                self.procesos.append([nombre, int(''.join(filter(str.isdigit, tamaño)))])

    def primera(self):
        self.reinicio()
        for proceso in self.procesos:
            for i, element in enumerate(self.memoria):
                if proceso[1] < element[0]:
                    self.memoria[i][0] -= proceso[1]
                    self.memoria[i].append(proceso)
                    break
        self.gradiente()

    def mejor(self):
        self.reinicio()
        for proceso in self.procesos:
            mejor = None
            for i, elemento in enumerate(self.memoria):
                if proceso[1] <=elemento[0] and (mejor is None or elemento[0] < self.memoria[mejor][0]):
                    mejor = i
            
            if mejor is not None:
                self.memoria[mejor][0] -= proceso[1]
                self.memoria[mejor].append(proceso)
        self.gradiente()

    def peor(self):
        self.reinicio()
        for proceso in self.procesos:
            mayor = 0
            indice = None
            for i, elemento in enumerate(self.memoria):
                if proceso[1] < elemento[0] and elemento[0] > mayor:
                    mayor = elemento[0]
                    indice = i
            
            if indice is not None:
                self.memoria[indice][0] -= proceso[1]
                self.memoria[indice].append(proceso)
        self.gradiente()


    def siguiente(self):
        self.reinicio()
        for proceso in self.procesos:
            for i in range(len(self.memoria)):
                indice_actual = (i + self.indice) % len(self.memoria)
                bloque = self.memoria[indice_actual]
            
                if proceso[1] <= bloque[0]:
                    self.memoria[indice_actual][0] -= proceso[1]
                    self.memoria[indice_actual].append(proceso)
                    self.indice = indice_actual
                    break
        self.gradiente()

    ###############################################  GUI  ##################################################################
    def gradiente(self): 
        for i, elemento in enumerate(self.memoria):
            text = ""
            for archivo in elemento[1:]:
                text += archivo[0] + ' = ' + str(archivo[1]) + ' Kb.\n'
            text += str(elemento[0]) + ' Kb Libres.'
            if i == 0 and len(elemento)>1:  
                g = elemento[0]/1000  
                self.L_1000.setText(text)
                self.L_1000.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:{g} rgba(170, 255, 255, 100), stop:{g+0.0001} rgba(0, 255, 127, 100));")
            elif i == 1 and len(elemento)>1: 
                g = elemento[0]/400       
                self.L_400.setText(text)
                self.L_400.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:{g} rgba(170, 255, 255, 100), stop:{g+0.0001} rgba(0, 255, 127, 100));")
            elif i == 2 and len(elemento)>1:
                g = elemento[0]/1800        
                self.L_1800.setText(text)
                self.L_1800.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:{g} rgba(170, 255, 255, 100), stop:{g+0.0001} rgba(0, 255, 127, 100));")
            elif i == 3 and len(elemento)>1:
                g = elemento[0]/700        
                self.L_700.setText(text)
                self.L_700.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:{g} rgba(170, 255, 255, 100), stop:{g+0.0001} rgba(0, 255, 127, 100));")
            elif i == 4 and len(elemento)>1:
                g = elemento[0]/900        
                self.L_900.setText(text)
                self.L_900.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:{g} rgba(170, 255, 255, 100), stop:{g+0.0001} rgba(0, 255, 127, 100));")
            elif i == 5 and len(elemento)>1:
                g = elemento[0]/1200        
                self.L_1200.setText(text)
                self.L_1200.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:{g} rgba(170, 255, 255, 100), stop:{g+0.0001} rgba(0, 255, 127, 100));")
            elif i == 6 and len(elemento)>1:
                g = elemento[0]/1500        
                self.L_1500.setText(text)
                self.L_1500.setStyleSheet(f"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:{g} rgba(170, 255, 255, 100), stop:{g+0.0001} rgba(0, 255, 127, 100));")      

    def reinicio(self):
        self.memoria = [[1000], [400], [1800], [700], [900], [1200], [1500]]
        self.indice = 0
        self.L_1000.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_1000.setText("1000 Kb")
        self.L_400.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_400.setText("400 Kb")
        self.L_1800.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_1800.setText("1800 Kb")
        self.L_700.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_700.setText("700 Kb")
        self.L_900.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_900.setText("900 Kb")
        self.L_1200.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_1200.setText("1200 Kb")
        self.L_1500.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_1500.setText("1500 Kb")
        
    def font_button(self):
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(70)
        return font
    
    def font_label(self):
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        return font
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(600, 905)
        MainWindow.setWindowTitle("ACT5: ADMINISTRADOR DE MEMORIA 1")
        MainWindow.setWindowIcon(QtGui.QIcon(str('./AppIcon.ico')))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.L_1000 = QtWidgets.QLabel(self.centralwidget)
        self.L_1000.setGeometry(QtCore.QRect(0, 0, 350, 120))
        self.L_1000.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_1000.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.L_1000.setFont(self.font_label())
        self.L_1000.setText("1000 Kb")
        self.L_1000.setAlignment(QtCore.Qt.AlignCenter)
        
        self.L_400 = QtWidgets.QLabel(self.centralwidget)
        self.L_400.setGeometry(QtCore.QRect(0, 120, 350, 42))
        self.L_400.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_400.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.L_400.setFont(self.font_label())
        self.L_400.setText("400 Kb")
        self.L_400.setAlignment(QtCore.Qt.AlignCenter)

        self.L_1800 = QtWidgets.QLabel(self.centralwidget)
        self.L_1800.setGeometry(QtCore.QRect(0, 162, 350, 224))
        self.L_1800.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_1800.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.L_1800.setFont(self.font_label())
        self.L_1800.setText("1800 Kb")
        self.L_1800.setAlignment(QtCore.Qt.AlignCenter)

        self.L_700 = QtWidgets.QLabel(self.centralwidget)
        self.L_700.setGeometry(QtCore.QRect(0, 386, 350, 81))
        self.L_700.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_700.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.L_700.setFont(self.font_label())
        self.L_700.setText("700 Kb")
        self.L_700.setAlignment(QtCore.Qt.AlignCenter)

        self.L_900 = QtWidgets.QLabel(self.centralwidget)
        self.L_900.setGeometry(QtCore.QRect(0, 467, 350, 107))
        self.L_900.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_900.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.L_900.setFont(self.font_label())
        self.L_900.setText("900 Kb")
        self.L_900.setAlignment(QtCore.Qt.AlignCenter)

        self.L_1200 = QtWidgets.QLabel(self.centralwidget)
        self.L_1200.setGeometry(QtCore.QRect(0, 574, 350, 146))
        self.L_1200.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_1200.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.L_1200.setFont(self.font_label())
        self.L_1200.setText("1200 Kb")
        self.L_1200.setAlignment(QtCore.Qt.AlignCenter)

        self.L_1500 = QtWidgets.QLabel(self.centralwidget)
        self.L_1500.setGeometry(QtCore.QRect(0, 720, 350, 185))
        self.L_1500.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_1500.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.L_1500.setFont(self.font_label())
        self.L_1500.setText("1500 Kb")
        self.L_1500.setAlignment(QtCore.Qt.AlignCenter)

        self.B_primer = QtWidgets.QRadioButton(self.centralwidget)
        self.B_primer.setGeometry(QtCore.QRect(360, 400, 260, 20))
        self.B_primer.setFont(self.font_button())
        self.B_primer.setText("PRIMER AJUSTE")

        self.B_mejor = QtWidgets.QRadioButton(self.centralwidget)
        self.B_mejor.setGeometry(QtCore.QRect(360, 430, 260, 20))
        self.B_mejor.setFont(self.font_button())
        self.B_mejor.setText("MEJOR AJUSTE")

        self.B_peor = QtWidgets.QRadioButton(self.centralwidget)
        self.B_peor.setGeometry(QtCore.QRect(360, 460, 260, 20))
        self.B_peor.setFont(self.font_button())
        self.B_peor.setText("PEOR AJUSTE")

        self.B_siguiente = QtWidgets.QRadioButton(self.centralwidget)
        self.B_siguiente.setGeometry(QtCore.QRect(360, 490, 260, 20))
        self.B_siguiente.setFont(self.font_button())
        self.B_siguiente.setText("SIGUIENTE AJUSTE")

        #self.B_reinicio = QtWidgets.QRadioButton(self.centralwidget)
        #self.B_reinicio.setGeometry(QtCore.QRect(360, 520, 260, 20))
        #self.B_reinicio.setFont(self.font_button())
        #self.B_reinicio.setText("REINICIO MEMORIA")

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

####################### LLAMADAS A FUCNIONES #########################################

        self.B_primer.toggled.connect(self.primera)
        self.B_mejor.toggled.connect(self.mejor)
        self.B_peor.toggled.connect(self.peor)
        self.B_siguiente.toggled.connect(self.siguiente)
        self.B_reinicio.toggled.connect(self.reinicio)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.archivo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
