from PyQt5.QtWidgets import QDialog
from PyQt5 import uic, QtSql


class GPPForm(QDialog):
    def __init__(self):
        super(GPPForm, self).__init__()
        uic.loadUi("./ui/GPPform.ui", self)
        self.load_table()
        self.tVGPP.setModel(self.model)

    def load_table(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("gpp")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        print(self.model.select())
