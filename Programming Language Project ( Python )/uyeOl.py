# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uyeOl.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Form(object):
    def insertUyeOl(self):
        TCNO=self.tcNo_2.text().format(int)
        sifre=self.sifre.text().format(str)
        email=self.tcNo_3.text().format(str)
        Name=self.isim.text().format(str)
        Surname=self.soyIsim.text().format(str)
        telefon=self.telefon.text().format(str)

        dataBase = sqlite3.connect('davaBilgiSistemi.db')
        dataBase.execute('''
        INSERT INTO uyeOl(TCNO,Name,Surname,sifre,email,telefon) VALUES(?,?,?,?,?,?)    
        ''',( int(TCNO[0]),Name,Surname,sifre,email,telefon))
        dataBase.commit()
        dataBase.close()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(797, 434)
        Form.setStyleSheet("background-color:#F7EDC0;\n"
"color:black")
        self.sifre = QtWidgets.QLineEdit(Form)
        self.sifre.setGeometry(QtCore.QRect(190, 140, 151, 20))
        self.sifre.setObjectName("sifre")
        self.uyeOl = QtWidgets.QPushButton(Form)
        self.uyeOl.setGeometry(QtCore.QRect(320, 320, 101, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.uyeOl.setFont(font)
        self.uyeOl.setObjectName("uyeOl")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(120, 140, 61, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.geriDon = QtWidgets.QPushButton(Form)
        self.geriDon.setGeometry(QtCore.QRect(20, 30, 91, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.geriDon.setFont(font)
        self.geriDon.setObjectName("geriDon")
        self.tcNo_2 = QtWidgets.QLineEdit(Form)
        self.tcNo_2.setGeometry(QtCore.QRect(190, 100, 151, 20))
        self.tcNo_2.setObjectName("tcNo_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(120, 100, 47, 13))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(310, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.sifreTekrar = QtWidgets.QLineEdit(Form)
        self.sifreTekrar.setGeometry(QtCore.QRect(190, 180, 151, 20))
        self.sifreTekrar.setObjectName("sifreTekrar")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(70, 180, 111, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tcNo_3 = QtWidgets.QLineEdit(Form)
        self.tcNo_3.setGeometry(QtCore.QRect(190, 220, 151, 20))
        self.tcNo_3.setObjectName("tcNo_3")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(120, 220, 51, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.telefon = QtWidgets.QLineEdit(Form)
        self.telefon.setGeometry(QtCore.QRect(500, 220, 151, 20))
        self.telefon.setObjectName("telefon")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(410, 220, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(430, 100, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.isim = QtWidgets.QLineEdit(Form)
        self.isim.setGeometry(QtCore.QRect(500, 100, 151, 20))
        self.isim.setObjectName("isim")
        self.soyIsim = QtWidgets.QLineEdit(Form)
        self.soyIsim.setGeometry(QtCore.QRect(500, 140, 151, 20))
        self.soyIsim.setObjectName("soyIsim")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(410, 140, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(400, 180, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(500, 180, 82, 17))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(570, 180, 82, 17))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.geriDon.clicked.connect(Form.close)
        self.retranslateUi(Form)

        self.uyeOl.clicked.connect(self.insertUyeOl)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.uyeOl.setText(_translate("Form", "Üye Ol"))
        self.label_4.setText(_translate("Form", "Şifre :"))
        self.geriDon.setText(_translate("Form", "Kapat"))
        self.label_5.setText(_translate("Form", "TC NO:"))
        self.label_6.setText(_translate("Form", "Üye Ol"))
        self.label_7.setText(_translate("Form", "Şifre Tekrar:"))
        self.label_8.setText(_translate("Form", "Email :"))
        self.label_9.setText(_translate("Form", "Telefon :"))
        self.label_10.setText(_translate("Form", "İsim :"))
        self.label_11.setText(_translate("Form", "Soyisim :"))
        self.label_12.setText(_translate("Form", "Cinsiyet :"))
        self.radioButton.setText(_translate("Form", "Erkek"))
        self.radioButton_2.setText(_translate("Form", "Kız"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())