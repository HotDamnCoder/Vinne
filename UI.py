# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 309)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OutputTextBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.OutputTextBox.setGeometry(QtCore.QRect(220, 0, 421, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutputTextBox.sizePolicy().hasHeightForWidth())
        self.OutputTextBox.setSizePolicy(sizePolicy)
        self.OutputTextBox.setStyleSheet("font: 10pt \"Segoe UI Semilight\";")
        self.OutputTextBox.setObjectName("OutputTextBox")
        self.InputTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.InputTextBox.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.InputTextBox.setFont(font)
        self.InputTextBox.setAlignment(QtCore.Qt.AlignCenter)
        self.InputTextBox.setObjectName("InputTextBox")
        self.LaoLagedaleButton = QtWidgets.QPushButton(self.centralwidget)
        self.LaoLagedaleButton.setGeometry(QtCore.QRect(50, 190, 111, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.LaoLagedaleButton.setFont(font)
        self.LaoLagedaleButton.setObjectName("LaoLagedaleButton")
        self.ThjendaButton = QtWidgets.QPushButton(self.centralwidget)
        self.ThjendaButton.setGeometry(QtCore.QRect(60, 220, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.ThjendaButton.setFont(font)
        self.ThjendaButton.setObjectName("ThjendaButton")
        self.Vinne = QtWidgets.QLabel(self.centralwidget)
        self.Vinne.setGeometry(QtCore.QRect(0, 30, 251, 251))
        self.Vinne.setStyleSheet("border-image: url(:/Images/download.jpg);")
        self.Vinne.setObjectName("Vinne")
        self.Hall = QtWidgets.QLabel(self.centralwidget)
        self.Hall.setGeometry(QtCore.QRect(0, 0, 251, 31))
        self.Hall.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.Hall.setObjectName("Hall")
        self.Hall.raise_()
        self.Vinne.raise_()
        self.OutputTextBox.raise_()
        self.InputTextBox.raise_()
        self.LaoLagedaleButton.raise_()
        self.ThjendaButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ElektronSkeem"))
        self.InputTextBox.setPlaceholderText(_translate("MainWindow", "Elektronide arv"))
        self.LaoLagedaleButton.setText(_translate("MainWindow", "Lao Lagedale!"))
        self.ThjendaButton.setText(_translate("MainWindow", "Tühjenda"))
import resources_rc
