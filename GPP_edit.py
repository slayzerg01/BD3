from PyQt5.QtWidgets import QDialog
from PyQt5 import uic, QtSql


class GPP_edit(QDialog):
    def __init__(self):
        super(GPP_edit, self).__init__()
        uic.loadUi("./ui/GPPedit.ui", self)
        self.setWindowModality(2)
