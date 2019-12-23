# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'girisSayfasi.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import hakkinda
import adminGiris
import uyeOl
import uyeSayfasi
import sqlite3

class Ui_Form(object):

    def giriss(self):
        tcNo=self.tcNo.text().format(str)
        sifre=self.sifre.text().format(str)
        database = sqlite3.connect('davaBilgiSistemi.db')
        result = database.execute('''Select TCNO,sifre from uyeOl where TCNO=? AND sifre=?''', (tcNo, sifre))
        if (len(result.fetchall()) > 0):
            self.window = QtWidgets.QWidget()
            self.ui = uyeSayfasi.Ui_Form()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            print("Bilgiler başarısız")
    def uyeOll(self):
        self.window = QtWidgets.QWidget()
        self.ui = uyeOl.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def adminGiriss(self):
        self.window = QtWidgets.QWidget()
        self.ui = adminGiris.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def hakkindaa(self):
        self.window = QtWidgets.QWidget()
        self.ui = hakkinda.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(381, 297)
        Form.setStyleSheet("background-color:#F7EDC0;\n"
"color:black")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 80, 47, 13))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 61, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tcNo = QtWidgets.QLineEdit(Form)
        self.tcNo.setGeometry(QtCore.QRect(150, 80, 151, 20))
        self.tcNo.setObjectName("tcNo")
        self.sifre = QtWidgets.QLineEdit(Form)
        self.sifre.setGeometry(QtCore.QRect(150, 120, 151, 20))
        self.sifre.setObjectName("sifre")
        self.girisYap = QtWidgets.QPushButton(Form)
        self.girisYap.setGeometry(QtCore.QRect(50, 180, 91, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.girisYap.setFont(font)
        self.girisYap.setObjectName("girisYap")
        self.uyeOl = QtWidgets.QPushButton(Form)
        self.uyeOl.setGeometry(QtCore.QRect(220, 180, 101, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.uyeOl.setFont(font)
        self.uyeOl.setObjectName("uyeOl")
        self.hakkinda = QtWidgets.QPushButton(Form)
        self.hakkinda.setGeometry(QtCore.QRect(50, 220, 91, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.hakkinda.setFont(font)
        self.hakkinda.setObjectName("hakkinda")
        self.adminGiris = QtWidgets.QPushButton(Form)
        self.adminGiris.setGeometry(QtCore.QRect(220, 220, 101, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.adminGiris.setFont(font)
        self.adminGiris.setObjectName("adminGiris")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.girisYap.clicked.connect(self.giriss)
        self.uyeOl.clicked.connect(self.uyeOll)
        self.hakkinda.clicked.connect(self.hakkindaa)
        self.adminGiris.clicked.connect(self.adminGiriss)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TC NO:"))
        self.label_2.setText(_translate("Form", "Şifre :"))
        self.girisYap.setText(_translate("Form", "Giriş Yap"))
        self.uyeOl.setText(_translate("Form", "Üye Ol"))
        self.hakkinda.setText(_translate("Form", "Hakkında"))
        self.adminGiris.setText(_translate("Form", "Admin Giriş"))
        self.label_3.setText(_translate("Form", "Dava Bilgi Sistemi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
