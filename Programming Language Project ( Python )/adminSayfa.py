# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminSayfa.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_Form(object):
    def insertDavalar(self):

        DavaciTC=self.davaciTC.text().format(str)
        DavaliTC=self.davaliTC.text().format(str)
        Detaylar=self.davaAdi.text().format(str)
        DavaAdi=self.detaylar.toPlainText()

        dataBase = sqlite3.connect('davaBilgiSistemi.db')
        dataBase.execute('''
        INSERT INTO Davalar(DavaciTC,DavaliTC,Detaylar,DavaAdi) VALUES(?,?,?,?)    
        ''', (DavaciTC,DavaliTC,Detaylar,DavaAdi))
        dataBase.commit()
        dataBase.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(818, 451)
        Form.setStyleSheet("background-color:#F7EDC0;\n"
"color:black")
        self.cikis = QtWidgets.QPushButton(Form)
        self.cikis.setGeometry(QtCore.QRect(670, 390, 101, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.cikis.setFont(font)
        self.cikis.setObjectName("cikis")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(310, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.davaciTC = QtWidgets.QLineEdit(Form)
        self.davaciTC.setGeometry(QtCore.QRect(110, 60, 151, 20))
        self.davaciTC.setObjectName("davaciTC")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(490, 50, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.davaliTC = QtWidgets.QLineEdit(Form)
        self.davaliTC.setGeometry(QtCore.QRect(580, 50, 151, 20))
        self.davaliTC.setObjectName("davaliTC")
        self.detaylar = QtWidgets.QTextEdit(Form)
        self.detaylar.setGeometry(QtCore.QRect(120, 120, 531, 231))
        self.detaylar.setObjectName("detaylar")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 120, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.ekle = QtWidgets.QPushButton(Form)
        self.ekle.setGeometry(QtCore.QRect(320, 380, 101, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.ekle.setFont(font)
        self.ekle.setObjectName("ekle")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(280, 90, 81, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.davaAdi = QtWidgets.QLineEdit(Form)
        self.davaAdi.setGeometry(QtCore.QRect(370, 90, 151, 20))
        self.davaAdi.setObjectName("davaAdi")
        self.ekle.clicked.connect(self.insertDavalar)
        self.cikis.clicked.connect(Form.close)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cikis.setText(_translate("Form", "Çıkış"))
        self.label_6.setText(_translate("Form", "Dava Ekle"))
        self.label_7.setText(_translate("Form", "Davacı TC:"))
        self.label_8.setText(_translate("Form", "Davalı TC:"))
        self.label_9.setText(_translate("Form", "Detaylar :"))
        self.ekle.setText(_translate("Form", "Ekle"))
        self.label_10.setText(_translate("Form", "Dava :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
