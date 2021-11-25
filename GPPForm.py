from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import uic, QtSql, QtCore
from GPP_edit import GPP_edit


class GPPForm(QDialog):
    def __init__(self):
        super(GPPForm, self).__init__()
        uic.loadUi("./ui/GPPform.ui", self)
        self.load_table()
        self.setWindowModality(2)
        self.tVGPP.setModel(self.model)
        self.pB_save.clicked.connect(self.save_changes)
        self.pB_add.clicked.connect(self.add_data)
        self.pB_remove.clicked.connect(self.remove_data)
        self.tVGPP.doubleClicked.connect(self.edit_data)

        self.tVGPP.hideColumn(0)
        # self.tVGPP.verticalHeader().setVisible(False)
        self.tVGPP.resizeColumnsToContents()

    def remove_data(self):
        cur_row = self.tVGPP.currentIndex().row()
        if QMessageBox.question(self, "Подтвердите удаление", "Вы действительно хотите удалить сотрудника "
                                                              + self.model.record(cur_row).value("FIO") + "?",
                                QMessageBox.Cancel, QMessageBox.Ok) == QMessageBox.Ok:
            self.model.removeRow(cur_row)
            if not self.model.submitAll():
                QMessageBox.critical(self, "Ошибка", self.model.lastError().text(), QMessageBox.Ok)

    def edit_data(self):
        cur_row = self.tVGPP.currentIndex().row()
        self.GPP_edit = GPP_edit()
        self.GPP_edit.lE_FIO.setText(self.model.record(cur_row).value("FIO"))
        self.GPP_edit.lE_Pos.setText(self.model.record(cur_row).value("position"))
        self.GPP_edit.lE_Edu.setText(self.model.record(cur_row).value("education"))
        self.GPP_edit.lE_Adr.setText(self.model.record(cur_row).value("address"))
        self.GPP_edit.lE_Num.setText(self.model.record(cur_row).value("phone_number"))
        if self.GPP_edit.exec_():
            self.model.setData(self.model.index(cur_row, 1), self.GPP_edit.lE_FIO.text())
            self.model.setData(self.model.index(cur_row, 2), self.GPP_edit.lE_Pos.text())
            self.model.setData(self.model.index(cur_row, 3), self.GPP_edit.lE_Edu.text())
            self.model.setData(self.model.index(cur_row, 4), self.GPP_edit.lE_Adr.text())
            self.model.setData(self.model.index(cur_row, 5), self.GPP_edit.lE_Num.text())

    def add_data(self):
        self.GPP_edit = GPP_edit()
        if self.GPP_edit.exec_():
            record = self.model.record()
            record.remove(0)
            record.setValue("FIO", self.GPP_edit.lE_FIO.text())
            record.setValue("position", self.GPP_edit.lE_Pos.text())
            record.setValue("education", self.GPP_edit.lE_Edu.text())
            record.setValue("address", self.GPP_edit.lE_Adr.text())
            record.setValue("phone_number", self.GPP_edit.lE_Num.text())
            self.model.insertRecord(-1, record)

    def load_table(self):
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("sotr_gpp")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        print(self.model.select())
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "ФИО")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Должность")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Образование")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Адрес")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Номер тел.")

    def save_changes(self):
        self.model.submitAll()
