from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog
from PyQt5 import uic


class GPPForm(QDialog):
    def __init__(self):
        super(GPPForm, self).__init__()
        uic.loadUi("./ui/GPPform.ui", self)
