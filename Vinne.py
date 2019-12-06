# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from Generate_Table import *
from UI import Ui_MainWindow


class MainW (QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Button.clicked.connect(self.PrintSomething)

    def PrintSomething(self):
        electrons = int(self.InputTextBox.text())
        orbital_amount = generate_orbital_needs(electrons)
        orbital_names = generate_orbital_layer_names(0, orbital_amount)
        table = generate_table(orbital_names[:])
        orb_values = generate_orbital_values(orbital_names)
        electron_sch = create_electron_scheme(table, electrons, orb_values)
        Last_electrons, Nr_of_shells, element_kind, square_scheme = read_electron_scheme(electron_sch, orb_values)
        html = "Elektron skeem: " + electron_sch + "\n" + "Väliskihis elektronide arv: " + Last_electrons + "\n" + "Elektronkihtide arv: " + Nr_of_shells + "\n" + "Elemendi tüüp: " + element_kind + "\n" + "Väliskihi ruutskeem: "
        for square in square_scheme:
            html += "\n" + square
        self.OutputTextBox.setText(html)
        write_info_to_file(electron_sch, Last_electrons, Nr_of_shells, element_kind,square_scheme)


app = QApplication(sys.argv)
myapp = MainW()
myapp.show()
sys.exit(app.exec_())

