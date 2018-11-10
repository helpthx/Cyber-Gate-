# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_3_green.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Monitor(object):
    def setupUi(self, Monitor):
        Monitor.setObjectName(_fromUtf8("Monitor"))
        Monitor.resize(620, 700)
        Monitor.setMaximumSize(QtCore.QSize(620, 700))
        self.centralwidget = QtGui.QWidget(Monitor)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Nome = QtGui.QTextBrowser(self.centralwidget)
        self.Nome.setGeometry(QtCore.QRect(30, 350, 571, 81))
        self.Nome.setObjectName(_fromUtf8("Nome"))
        self.Matricula = QtGui.QTextBrowser(self.centralwidget)
        self.Matricula.setGeometry(QtCore.QRect(30, 460, 301, 51))
        self.Matricula.setObjectName(_fromUtf8("Matricula"))
        self.Dinheiro = QtGui.QTextBrowser(self.centralwidget)
        self.Dinheiro.setGeometry(QtCore.QRect(340, 460, 261, 51))
        self.Dinheiro.setObjectName(_fromUtf8("Dinheiro"))
        self.Matricula_l = QtGui.QLabel(self.centralwidget)
        self.Matricula_l.setGeometry(QtCore.QRect(30, 440, 71, 17))
        self.Matricula_l.setObjectName(_fromUtf8("Matricula_l"))
        self.DInheiro_l = QtGui.QLabel(self.centralwidget)
        self.DInheiro_l.setGeometry(QtCore.QRect(340, 440, 131, 17))
        self.DInheiro_l.setObjectName(_fromUtf8("DInheiro_l"))
        self.Nome_L = QtGui.QLabel(self.centralwidget)
        self.Nome_L.setGeometry(QtCore.QRect(30, 330, 131, 17))
        self.Nome_L.setObjectName(_fromUtf8("Nome_L"))
        self.Data_e_HOra = QtGui.QDateTimeEdit(self.centralwidget)
        self.Data_e_HOra.setGeometry(QtCore.QRect(410, 530, 194, 27))
        self.Data_e_HOra.setObjectName(_fromUtf8("Data_e_HOra"))
        self.Status = QtGui.QTextBrowser(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(30, 560, 571, 81))
        self.Status.setObjectName(_fromUtf8("Status"))
        self.Status_l = QtGui.QLabel(self.centralwidget)
        self.Status_l.setGeometry(QtCore.QRect(30, 540, 66, 17))
        self.Status_l.setObjectName(_fromUtf8("Status_l"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(180, 10, 275, 320))
        self.textBrowser.setMinimumSize(QtCore.QSize(275, 320))
        self.textBrowser.setMaximumSize(QtCore.QSize(275, 320))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        Monitor.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Monitor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Monitor.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Monitor)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Monitor.setStatusBar(self.statusbar)

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        Monitor.setWindowTitle(_translate("Monitor", "Monitor", None))
        self.Nome.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">João Vitor Rodrigues Baptista</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:22pt; font-weight:600;\"><br /></p></body></html>", None))
        self.Matricula.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">150013329</span></p></body></html>", None))
        self.Dinheiro.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">R$ 5.20</span></p></body></html>", None))
        self.Matricula_l.setText(_translate("Monitor", "Matrícula: ", None))
        self.DInheiro_l.setText(_translate("Monitor", "Saldo Atual:", None))
        self.Nome_L.setText(_translate("Monitor", "Nome:", None))
        self.Status.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#00aa00;\">ACESSO PERMITIDO</span></p></body></html>", None))
        self.Status_l.setText(_translate("Monitor", "Status:", None))
        self.textBrowser.setHtml(_translate("Monitor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/PIC/cortado.png\" /></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Monitor = QtGui.QMainWindow()
    ui = Ui_Monitor()
    ui.setupUi(Monitor)
    Monitor.show()
    sys.exit(app.exec_())

