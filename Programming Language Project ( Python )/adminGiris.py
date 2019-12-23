# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminGiris.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import adminSayfa

class Ui_Form(object):
    def checkUser(self):
        if (self.tcNo.text().format(str)=="134" and self.sifre.text().format(str)=="123"):
            self.window = QtWidgets.QWidget()
            self.ui = adminSayfa.Ui_Form()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            print("Yanlış Bilgiler")
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color:#F7EDC0;\n"
"color:black")
        self.kapat = QtWidgets.QPushButton(Form)
        self.kapat.setGeometry(QtCore.QRect(140, 220, 91, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.kapat.setFont(font)
        self.kapat.setObjectName("kapat")
        self.girisYap = QtWidgets.QPushButton(Form)
        self.girisYap.setGeometry(QtCore.QRect(140, 180, 91, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.girisYap.setFont(font)
        self.girisYap.setObjectName("girisYap")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(130, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.sifre = QtWidgets.QLineEdit(Form)
        self.sifre.setGeometry(QtCore.QRect(160, 120, 151, 20))
        self.sifre.setObjectName("sifre")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 120, 61, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(90, 80, 47, 13))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tcNo = QtWidgets.QLineEdit(Form)
        self.tcNo.setGeometry(QtCore.QRect(160, 80, 151, 20))
        self.tcNo.setObjectName("tcNo")
        self.kapat.clicked.connect(Form.close)
        self.girisYap.clicked.connect(self.checkUser)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.kapat.setText(_translate("Form", "Kapat"))
        self.girisYap.setText(_translate("Form", "Giriş Yap"))
        self.label_6.setText(_translate("Form", "Admin Girişi"))
        self.label_4.setText(_translate("Form", "Şifre :"))
        self.label_5.setText(_translate("Form", "TC NO:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
