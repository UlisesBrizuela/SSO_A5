#ACTIVIDAD 5 - SEMINARIO DE SOLUCION DE PROBLEMAS DE SISTEMAS OPERATIVOS
#BRIZUELA ARIAS ULISES ISRAEL

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):


    ###############################################  GUI  ##################################################################
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
        self.L_700.setText(" 700 Kb")
        self.L_700.setAlignment(QtCore.Qt.AlignCenter)

        self.L_900 = QtWidgets.QLabel(self.centralwidget)
        self.L_900.setGeometry(QtCore.QRect(0, 467, 350, 107))
        self.L_900.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_900.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.L_900.setFont(self.font_label())
        self.L_900.setText("900 Kb")
        self.L_900.setAlignment(QtCore.Qt.AlignCenter)

        self.L_1350 = QtWidgets.QLabel(self.centralwidget)
        self.L_1350.setGeometry(QtCore.QRect(0, 574, 350, 146))
        self.L_1350.setStyleSheet("background-color: rgba(170, 255, 255, 100);")
        self.L_1350.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.L_1350.setFont(self.font_label())
        self.L_1350.setText("1350 Kb")
        self.L_1350.setAlignment(QtCore.Qt.AlignCenter)

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

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# COLOR GRADIAL PARA TAMAÑO DE ARCHIVO background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:0, stop:0.5 rgba(0, 255, 127, 100), stop:0.5001 rgba(170, 255, 255, 100));

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
