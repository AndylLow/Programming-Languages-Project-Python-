# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hakkinda.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color:#F7EDC0;\n"
"color:black")
        self.kapat = QtWidgets.QPushButton(Form)
        self.kapat.setGeometry(QtCore.QRect(150, 230, 91, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.kapat.setFont(font)
        self.kapat.setObjectName("kapat")
        self.kapat.clicked.connect(Form.close)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(140, 30, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(60, 70, 271, 131))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.kapat.setText(_translate("Form", "Kapat"))
        self.label_6.setText(_translate("Form", "Hakkında"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">avukatbarosu.com olarak avukatların iletişim bilgilerinin müvekkiller veya avukat arayışında olan kişi/kişiler tarafından daha kolay bulunabilmesi amaçlanmaktadır. Bu amaç doğrultusunda, web sitemizdeki avukat bilgileri güncel tutulmaya çalışılmaktadır.</span><span style=\" font-family:\'Open-Sance,sans-serif\'; font-size:8pt; color:#333333; background-color:transparent;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Web sitemizde yer alan avukat bilgilerinin çoğunluğu ilgili baronun web sitesinden alınmaktadır. Bazı bilgilerde Avukat Ekle sayfamızdan avukatlarımızın kendi bilgileri eklemesiyle oluşmaktadır.</span><span style=\" font-family:\'Open-Sance,sans-serif\'; font-size:8pt; color:#333333; background-color:transparent;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">İlgili avukat sayfasındaki avukat isminin yanında bulunan işareti, avukatın bilgilerinin kendisinin eklediğini ve izni dahilinde yayınlanmakta olduğunu belirtir.</span><span style=\" font-family:\'Open-Sance,sans-serif\'; font-size:8pt; color:#333333; background-color:transparent;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Yanlış ya da hatalı bilgiler için, ilgili avukat sayfasındaki &quot;Avukat Düzelt&quot; butonunu kullanarak düzeltme yapabilir yada &quot;Sorun Bildir&quot; butonu ile sorun bildiriminde bulunabilirsiniz.</span><span style=\" font-family:\'Open-Sance,sans-serif\'; font-size:8pt; color:#333333; background-color:transparent;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Bilgilerinizin web sitemizde yer almasını istemiyorsanız, iletişim bölümünden bizlerle iletişim kurabilirsiniz.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
