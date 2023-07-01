from PyQt6 import QtCore, QtGui, QtWidgets
from turtle import *
from PIL import Image
import webbrowser


class Ui_mainWidget(object):
    def inicioTut(self):
        print("Se hizo clic en el botón 1")
        # función primer botón
        hideturtle()
        screensize(canvheight=500, canvwidth=500, bg="white")
        write(
            "FELIZ DÍA DEL PADRE, TE AMO MUCHO <3",
            align="Center",
            font=("Cooper Black", 20, "italic"),
        )
        print("Se hizo clic en el botón 1")
        speed(4)  # Configura la velocidad del dibujo
        penup()  # Levanta el lápiz para moverse sin dibujar
        goto(0, -200)  # Mueve la tortuga al centro de la ventana
        pendown()  # Baja el lápiz para comenzar a dibujar

        escala = 0.6
        # Dibujar el corazón
        color("red")  # Configura el color a rojo
        begin_fill()  # Comienza el llenado del corazón

        left(140)  # Gira la tortuga a la izquierda
        forward(224 * escala)  # Dibuja el lado izquierdo del corazón

        circle(-90 * escala, 200)  # Dibuja el arco superior del corazón

        left(120)  # Gira la tortuga para dibujar el lado derecho del corazón
        circle(-90 * escala, 200)  # Dibuja el arco derecho del corazón

        forward(224 * escala)  # Dibuja el lado derecho del corazón
        end_fill()
        exitonclick()

    def imagen(self):
        print("Se hizo clic en el botón 2")
        # función segundo botón
        imagenDir = "padre.png"
        imagen = Image.open(imagenDir)
        imagen.show()

    def abrirArchivo(self):
        print("Se hizo clic en el botón 3")
        webbrowser.open("mensaje.txt")

        # exitonclick()

    def setupUi(self, mainWidget):
        mainWidget.setObjectName("mainWidget")
        mainWidget.resize(250, 169)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(False)
        mainWidget.setFont(font)
        self.pushButton = QtWidgets.QPushButton(mainWidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.inicioTut)

        self.pushButton_2 = QtWidgets.QPushButton(mainWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.imagen)

        self.pushButton_3 = QtWidgets.QPushButton(mainWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.abrirArchivo)

        self.label = QtWidgets.QLabel(mainWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(mainWidget)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)

    def retranslateUi(self, mainWidget):
        _translate = QtCore.QCoreApplication.translate
        mainWidget.setWindowTitle(_translate("mainWidget", "PADRE"))
        self.pushButton.setText(_translate("mainWidget", "Inicio"))
        self.pushButton_2.setText(_translate("mainWidget", "Mi Padre"))
        self.pushButton_3.setText(_translate("mainWidget", "Léeme"))
        self.label.setText(_translate("mainWidget", "Día del Padre"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWidget = QtWidgets.QWidget()
    ui = Ui_mainWidget()
    ui.setupUi(mainWidget)
    mainWidget.show()
    sys.exit(app.exec())
