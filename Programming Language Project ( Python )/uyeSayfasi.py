# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uyeSayfasi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def changing(self,index):
        dataBase = sqlite3.connect('davaBilgiSistemi.db')
        result = dataBase.execute('''SELECT Detaylar FROM Davalar''')
        self.detaylar.setText(str(result[index]))
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(823, 432)
        Form.setStyleSheet("background-color:#F7EDC0;\n"
"color:black")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(40, 120, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.cikis = QtWidgets.QPushButton(Form)
        self.cikis.setGeometry(QtCore.QRect(690, 390, 101, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.cikis.setFont(font)
        self.cikis.setObjectName("cikis")
        self.detaylar = QtWidgets.QTextEdit(Form)
        self.detaylar.setGeometry(QtCore.QRect(140, 120, 531, 231))
        self.detaylar.setObjectName("detaylar")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(330, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.davalar = QtWidgets.QComboBox(Form)
        self.davalar.setGeometry(QtCore.QRect(260, 60, 231, 22))
        self.davalar.setObjectName("davalar")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(150, 60, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(600, 20, 181, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resim.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.cikis.clicked.connect(Form.close)
        self.retranslateUi(Form)

        dataBase = sqlite3.connect('davaBilgiSistemi.db')
        result=dataBase.execute('''SELECT DavaAdi FROM Davalar''')
        for x in result:
            self.davalar.addItems(x)

        self.davalar.currentIndexChanged.connect(self.changing,self.davalar.currentIndex())

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_11.setText(_translate("Form", "Detaylar :"))
        self.cikis.setText(_translate("Form", "Çıkış"))
        self.label_13.setText(_translate("Form", "Davalarım"))
        self.label_12.setText(_translate("Form", "Dava :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
