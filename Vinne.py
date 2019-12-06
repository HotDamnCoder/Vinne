# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import qtmodern.styles
import qtmodern.windows
from PyQt5.QtWidgets import *
import sys
from Generate_Table import *
from UI import Ui_MainWindow


class MainW (QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.LaoLagedaleButton.clicked.connect(self.print_out)
        self.ThjendaButton.clicked.connect(self.empty)

    def empty(self):
        self.InputTextBox.setText("")
        self.OutputTextBox.setText("")

    def print_out(self):
        electrons = int(self.InputTextBox.text())
        orbital_amount = generate_orbital_needs(electrons)
        orbital_names = generate_orbital_layer_names(0, orbital_amount)
        table = generate_table(orbital_names[:])
        orb_values = generate_orbital_values(orbital_names)
        electron_sch = create_electron_scheme(table, electrons, orb_values)
        last_electrons, nr_of_shells, element_kind, square_scheme = read_electron_scheme(electron_sch, orb_values)
        html = "Elektron skeem: " + electron_sch + "\n" + "Väliskihis elektronide arv: " + last_electrons + "\n" + "Elektronkihtide arv: " + nr_of_shells + "\n" + "Elemendi tüüp: " + element_kind + "\n" + "Väliskihi ruutskeem: "
        for square in square_scheme:
            html += "\n" + square
        self.OutputTextBox.setText(html)
        write_info_to_file(electron_sch, last_electrons, nr_of_shells, element_kind,square_scheme)


app = QApplication(sys.argv)
win = MainW()
qtmodern.styles.dark(app)
mw = qtmodern.windows.ModernWindow(win)
mw.show()
app.exec_()
