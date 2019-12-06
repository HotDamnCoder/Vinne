# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 272)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{border-image: url(:/Images/download.jpg) 0 0 0 0 stretch stretch;}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InputTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.InputTextBox.setGeometry(QtCore.QRect(9, 15, 133, 20))
        self.InputTextBox.setText("")
        self.InputTextBox.setObjectName("InputTextBox")
        self.OutputTextBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.OutputTextBox.setGeometry(QtCore.QRect(148, 15, 331, 211))
        self.OutputTextBox.setObjectName("OutputTextBox")
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setGeometry(QtCore.QRect(10, 50, 81, 23))
        self.Button.setObjectName("Button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ElektronSkeem"))
        self.InputTextBox.setWhatsThis(_translate("MainWindow", "Elektronide arv"))
        self.Button.setText(_translate("MainWindow", "Lao Lagedale!"))
import resources_rc
